# openapi_server/PasswordSecure/encode_password.py

import bcrypt

class PassEncrypt:
    def encode(self, password: str) -> str:
        passkey = password.encode('utf-8')
        hashed = bcrypt.hashpw(passkey, bcrypt.gensalt())
        return hashed.decode('utf-8')  # store as string in Firebase

    def verify(self, password: str, hashed: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
