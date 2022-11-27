from sqlalchemy.orm import Session
import models, schemas
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
import crud

JWT_SECRET = "markus"
ALGORITHM = "HS256"
from datetime import datetime, timedelta

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    # hash_pass = get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=user.password, username=user.username, is_active=user.is_active)
    # token = crud.create_access_token(db_user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"db_user": db_user}

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(title = item.title, description = item.description, owner_id=user_id)
    
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# def create_access_token(user):
#     print("useer", user.email)
#     try:
#         claims = {
#             "id": user.id,
#             "email": user.email,
#             "username": user.username,
#             "is_active": user.is_active,
#             "password": user.hashed_password,
#             "exp": datetime.utcnow() + timedelta(minutes=120),
#         }
#         return jwt.encode(claims=claims, key=JWT_SECRET, algorithm=ALGORITHM)
#     except Exception as ex:
#         print(str(ex))
#         raise ex

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)


# def get_password_hash(password):
#     return pwd_context.hash(password)

# def verify_token(token):
#     try:
#         payload = jwt.decode(token, key=JWT_SECRET)
#         print("1----------")
#         return payload
#     except:
#         print("2----------")
#         raise Exception("Wrong token")

# def check_active(token: str = Depends(oauth2_scheme)):
#     print("abc")
#     payload = verify_token(token)
#     active = payload.get("is_active")
#     print("3----------")
#     if not active:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Please activate your Account first",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     else:
#         return payload