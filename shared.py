import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import DictCursor
import logging
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from contextlib import contextmanager
import jwt
from jwt import ExpiredSignatureError, PyJWTError  # Update this line
from fastapi import Request  # Add this import

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"

# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')


@contextmanager
def get_db():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    try:
        yield conn
    finally:
        conn.close()


def init_db():
    with get_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                email TEXT PRIMARY KEY,
                login_count INTEGER DEFAULT 0
            )
            """)
        conn.commit()


async def record_user_login(email: str):
    with get_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
            INSERT INTO users (email, login_count) VALUES (%s, 1)
            ON CONFLICT (email) DO UPDATE SET login_count = users.login_count + 1
            """, (email,))
        conn.commit()
    logger.info(f"Login recorded for email: {email}")


async def get_user_count():
    with get_db() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM users")
            return cur.fetchone()[0]


async def get_total_logins():
    with get_db() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT SUM(login_count) FROM users")
            return cur.fetchone()[0] or 0

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
    logger.info(f"Token received: {token}")  # Add this line for debugging
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")  # Changed from "email" to "sub"
        if email is None:
            logger.error("Email claim is missing in the token")
            raise credentials_exception
        await record_user_login(email)  # Record the login
        return {"email": email, "name": payload.get("name")}
    except ExpiredSignatureError:
        logger.error("Token has expired")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except PyJWTError as e:  # Update this line
        logger.error(f"JWT error: {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")


async def get_optional_user(request: Request):
    token = request.cookies.get("access_token")
    if token and token.startswith("Bearer "):
        token = token[7:]  # Remove 'Bearer ' prefix
    if token:
        try:
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
            email: str = payload.get("sub")
            if email is None:
                logger.error("Email claim is missing in the token")
                return None
            return {"email": email, "name": payload.get("name")}
        except ExpiredSignatureError:
            logger.error("Token has expired")
        except PyJWTError as e:
            logger.error(f"JWT error: {e}")
    return None


def test_db_connection():
    try:
        with get_db() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
        logger.info("Database connection successful")
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        raise
