from fastapi import APIRouter, Request, HTTPException, status, Depends
from fastapi.responses import RedirectResponse
from jose import jwt
import os
from datetime import datetime, timedelta
import secrets
import httpx
import logging
from shared import logger, JWT_SECRET_KEY, ALGORITHM, record_user_login
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm

logger = logging.getLogger(__name__)

router = APIRouter()

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

# Determine the environment
IS_PRODUCTION = os.getenv("ENVIRONMENT") == "production"

# Set the appropriate redirect URI
if IS_PRODUCTION:
    GOOGLE_REDIRECT_URI = "https://learn-dsa-e9260d94725b.herokuapp.com/auth"
else:
    GOOGLE_REDIRECT_URI = "http://localhost:8000/auth"


ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.get('/login')
async def login(request: Request):
    state = secrets.token_urlsafe(16)
    auth_url = f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={GOOGLE_CLIENT_ID}&redirect_uri={GOOGLE_REDIRECT_URI}&scope=openid%20email%20profile&state={state}"
    logger.debug(f"Login URL: {auth_url}")
    logger.debug(f"Redirect URI: {GOOGLE_REDIRECT_URI}")
    logger.debug(f"Client ID: {GOOGLE_CLIENT_ID}")
    return RedirectResponse(url=auth_url)

@router.get('/auth')
async def auth(request: Request):
    code = request.query_params.get("code")
    state = request.query_params.get("state")
    error = request.query_params.get("error")

    logger.debug(f"Received code: {code}")
    logger.debug(f"Received state: {state}")
    logger.debug(f"Received error: {error}")

    if error:
        raise HTTPException(status_code=400, detail=f"Authorization error: {error}")

    if not code or not state:
        raise HTTPException(status_code=400, detail="Missing code or state")

    # Exchange code for token
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": GOOGLE_REDIRECT_URI
    }

    logger.debug(f"Token exchange request data: {data}")

    async with httpx.AsyncClient() as client:
        response = await client.post(token_url, data=data)
        if response.status_code != 200:
            error_detail = response.json()
            logger.error(f"Failed to retrieve token. Status: {response.status_code}, Details: {error_detail}")
            logger.error(f"Response headers: {response.headers}")
            logger.error(f"Full response content: {response.text}")  # Add this line
            if response.status_code == 401:
                raise HTTPException(status_code=400, detail=f"Unauthorized. Check your client ID and secret. Error: {error_detail}")
            raise HTTPException(status_code=400, detail=f"Failed to retrieve token: {error_detail}")
        token_data = response.json()

    # Get user info
    user_info_url = "https://www.googleapis.com/oauth2/v2/userinfo"
    headers = {"Authorization": f"Bearer {token_data['access_token']}"}

    async with httpx.AsyncClient() as client:
        response = await client.get(user_info_url, headers=headers)
        if response.status_code != 200:
            error_detail = response.json()
            logger.error(f"Failed to retrieve user info. Status: {response.status_code}, Details: {error_detail}")
            raise HTTPException(status_code=400, detail=f"Failed to retrieve user info: {error_detail}")
        user_info = response.json()

    # After successfully authenticating the user:
    user_email = user_info['email']
    logger.info(f"User authenticated: {user_email}")
    await record_user_login(user_email)

    # Create a JWT token
    access_token = create_access_token({"sub": user_info["email"], "name": user_info.get("name"), "email": user_info["email"]})
    
    redirect_url = f"/?token={access_token}"
    return RedirectResponse(url=redirect_url)

@router.get('/protected')
async def protected_route(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        return {"user": payload}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    access_token = create_access_token(data={"sub": user.username})
    logger.info(f"User logged in: {user.email}")
    await record_user_login(user.email)
    return {"access_token": access_token, "token_type": "bearer"}