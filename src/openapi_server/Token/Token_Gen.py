from datetime import datetime, timedelta

from firebase_admin import db
from jose import JWTError, jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from pydantic import BaseModel
import openapi_server.FirebaseAuth.Auth

SECRET_KEY = "09d25e094faa****************f7099f6f0f4caa6cf63b88e8d3e7"


ALGORITHM = "HS256"
class Token(BaseModel):
    access_token: str
    token_type: str


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def has_admin_login(token: str) -> bool:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("username")

        if not username:
            return False

        ref = db.reference("users")
        users = ref.get()

        if isinstance(users, list):
            users = {str(i): user for i, user in enumerate(users) if user}

        for user in users.values():
            if user.get("username") == username:
                return user.get("Role", "").lower() == "admin"

        return False

    except ExpiredSignatureError:
        print("Token has expired.")
        return False
    except InvalidTokenError:
        print("Invalid token.")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
