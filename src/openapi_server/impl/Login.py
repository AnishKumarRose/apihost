# openapi_server/services/login_impl.py

from firebase_admin import db
from loguru import logger

from openapi_server.PasswordSecure.encode_password import PassEncrypt
from openapi_server.Token.Token_Gen import Token, create_access_token
from openapi_server.models.user_create import UserCreate
from openapi_server.models.user_out import UserOut
import openapi_server.FirebaseAuth.Auth

passkey = PassEncrypt()

class LoginImpl:

    async def LoginDetails(self, username: str, password: str) -> Token:
        ref = db.reference('users')
        users = ref.get()

        if isinstance(users, list):
            users = {str(i): user for i, user in enumerate(users) if user}

        if not isinstance(users, dict):
            return Token(access_token="failed", token_type="Bearer")

        for uid, info in users.items():
            # logger.info([uid, info])
            if info.get("username") == username:
                stored_hash = info.get("password")
                role = info.get("Role")
                logger.info(role)
                if passkey.verify(password, stored_hash):
                    token = create_access_token(data={"username": username,"role": role})
                    return Token(access_token=token, token_type="Bearer")

        return Token(access_token="failed", token_type="Bearer")

    async def signup(self, request: UserCreate) -> UserOut:
        ref = db.reference('users')
        new_user_request = db.reference('user_add_request')
        users = ref.get() or {}
        logger.info(users)
        if isinstance(users, list):
            users = {str(i): user for i, user in enumerate(users) if user}


        if users:
            for uid, info in users.items():
                if info.get("username") == request.username:
                    raise ValueError("User already exists")
        existing_ids = [int(uid) for uid in users.keys() if uid.isdigit()]
        new_id = str(max(existing_ids) + 1) if existing_ids else "1"
        hashed_password = passkey.encode(request.password)
        # new_user_add =  ref.child(new_id)

        request = new_user_request.set(
            {
                "username": request.username,
                "password":hashed_password,
                "request":"pending"
            }
        )
        if request:
            return "Request Pending"

        # new_user_add.set({
        #     "username": request.username,
        #     "password": hashed_password,
        #     "Role":"user",
        #     "is_current": True
        # })

        # new_user_data = new_user_add.get()
        # return UserOut(
        #     id=new_id,
        #     username=new_user_data.get("username")
        # )
