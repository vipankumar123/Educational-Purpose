from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

JWT_SECRET = "markus"
ALGORITHM = "HS256"
from datetime import datetime, timedelta

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(user):
    try:
        claims = {
            "sub": user.username,
            "email": user.email,
            "role": user.role.value,
            "active": user.is_active,
            "exp": datetime.utcnow() + timedelta(minutes=120),
        }
        return jwt.encode(claims=claims, key=JWT_SECRET, algorithm=ALGORITHM)
    except Exception as ex:
        print(str(ex))
        raise ex