from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
from fastapi.security import OAuth2PasswordRequestForm


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, username=user.username)
    print("db_user", db_user)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    print("123")
    users = crud.get_users(db, skip=skip, limit=limit)
    print("123456")
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
    

# @app.post("/login")
# def login_user(
#     form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
# ):
#     db_user = crud.get_user_by_username(db=db, username=form_data.username)
#     if not db_user:
#         raise HTTPException(
#             status_code=401, detail="This email not found"
#         )

#     if crud.verify_password(form_data.password, db_user.hashed_password):
#         token = crud.create_access_token(db_user)
#         return {"access_token": token, "token_Type": "bearer"}
#     raise HTTPException(status_code=401, detail="password not matched!")






























# dependencies=[Depends(crud.check_active)]