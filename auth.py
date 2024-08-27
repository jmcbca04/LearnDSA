from fastapi import APIRouter, Request, HTTPException, status, Depends
from fastapi.responses import RedirectResponse
from jose import jwt
import os
from datetime import datetime, timedelta
import secrets
import httpx
from shared import logger, JWT_SECRET_KEY, ALGORITHM
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = "http://localhost:8000/auth"  # Update this to your actual redirect URI

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
    return RedirectResponse(url=auth_url)

@router.get('/auth')
async def auth(request: Request):
    code = request.query_params.get("code")
    state = request.query_params.get("state")

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

    async with httpx.AsyncClient() as client:
        response = await client.post(token_url, data=data)
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to retrieve token")
        token_data = response.json()

    # Get user info
    user_info_url = "https://www.googleapis.com/oauth2/v2/userinfo"
    headers = {"Authorization": f"Bearer {token_data['access_token']}"}

    async with httpx.AsyncClient() as client:
        response = await client.get(user_info_url, headers=headers)
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to retrieve user info")
        user_info = response.json()

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
