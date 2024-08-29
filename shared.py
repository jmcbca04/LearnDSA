from jose import jwt, JWTError, ExpiredSignatureError
import os
import logging
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
import sqlite3
from contextlib import contextmanager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"

DB_NAME = "user_logins.db"

@contextmanager
def get_db():
    conn = sqlite3.connect(DB_NAME)
    try:
        yield conn
    finally:
        conn.close()


def init_db():
    with get_db() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            email TEXT PRIMARY KEY,
            login_count INTEGER
        )
        """)


async def record_user_login(email: str):
    logger.info(f"Recording login for email: {email}")
    with get_db() as conn:
        conn.execute("""
        INSERT INTO users (email, login_count) VALUES (?, 1)
        ON CONFLICT(email) DO UPDATE SET login_count = login_count + 1
        """, (email,))
        conn.commit()
    logger.info("Login recorded successfully")


async def get_user_count():
    with get_db() as conn:
        return conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]


async def get_total_logins():
    with get_db() as conn:
        return conn.execute("SELECT SUM(login_count) FROM users").fetchone()[0] or 0

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token", auto_error=False)


async def get_current_user(token: str = Depends(oauth2_scheme)):
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
        email: str = payload.get("email")
        if email is None:
            logger.error("Email claim is missing in the token")
            raise credentials_exception
        await record_user_login(email)  # Record the login
        return {"email": email, "name": payload.get("name")}
    except ExpiredSignatureError:
        logger.error("Token has expired")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except JWTError as e:
        logger.error(f"JWT error: {e}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

async def get_optional_user(token: str = Depends(oauth2_scheme)):
    if token:
        try:
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
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
