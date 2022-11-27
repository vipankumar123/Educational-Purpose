from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import auth, crud, models, schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/register")
def register_user(user: schemas.UserSchema, db: Session = Depends(get_db)):
    # db_user = crud.get_users_by_username(db=db, username=user.username)
    # if db_user:
    #     raise HTTPException(status_code=400, detail="Email existiert bereits im System")
    db_user = crud.create_user(db=db, user=user)
    token = auth.create_access_token(db_user)
    return db_user


@app.post("/login")
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    db_user = crud.get_users_by_username(db=db, username=form_data.username)
    if not db_user:
        raise HTTPException(
            status_code=401, detail="Anmeldeinformationen nicht korrekt"
        )

    if auth.verify_password(form_data.password, db_user.hashed_password):
        token = auth.create_access_token(db_user)
        return {"access_token": token, "token_Type": "bearer"}
    raise HTTPException(status_code=401, detail="Anmeldeinformationen nicht korrekt")