from jose import jwt
import datetime
import os

secret_key = os.getenv("JWT_SECRET_KEY")
algorithm = "HS256"

payload = {
    "sub": "user@example.com",
    "name": "John Doe",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expires in 1 hour
}

token = jwt.encode(payload, secret_key, algorithm=algorithm)
print(token)