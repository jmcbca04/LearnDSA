from jose import jwt, JWTError, ExpiredSignatureError
import os
import logging
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"

logger.debug(f"JWT_SECRET_KEY: {JWT_SECRET_KEY}")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token", auto_error=False)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    logger.debug(f"Received token: {token}")
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if not token:
        logger.error("No token provided")
        raise credentials_exception
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        logger.debug(f"Decoded payload: {payload}")
        email: str = payload.get("email")
        if email is None:
            logger.error("Email claim is missing in the token")
            raise credentials_exception
        return {"email": email, "name": payload.get("name")}
    except ExpiredSignatureError:
        logger.error("Token has expired")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except JWTError as e:
        logger.error(f"JWT error: {e}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

async def get_optional_user(token: str = Depends(oauth2_scheme)):
    logger.debug(f"Received token: {token[:10] + '...' if token else None}")
    if token:
        try:
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
            logger.debug(f"Decoded payload: {payload}")
            email: str = payload.get("email")
            if email is None:
                logger.error("Email claim is missing in the token")
                return None
            return {"email": email, "name": payload.get("name")}
        except ExpiredSignatureError:
            logger.error("Token has expired")
            return None
        except JWTError as e:
            logger.error(f"JWT error: {e}")
            return None
    return None
