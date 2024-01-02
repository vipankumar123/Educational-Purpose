from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import *
from schemas import UserCreate
from crud import *

app = FastAPI()

Base.metadata.create_all(bind = engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/user/create")
async def create_user_api(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@app.get("/users/{user_id}")
async def read_user_api(user_id: int, db: Session = Depends(get_db)):
    db_user = read_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found!!")
    return db_user

@app.post("/user/update")
async def update_user_api(user_id: int,user: UserCreate, db: Session = Depends(get_db)):
    db_user = update_user(db, user_id, user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found!!")
    return db_user

@app.post("/user/delete")
async def delete_user_api(user_id: int, db: Session = Depends(get_db)):
    db_user = delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found!!")
    return db_user


