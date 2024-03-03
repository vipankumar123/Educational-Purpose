# main.py
from fastapi import FastAPI,Form, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from models import User
from database import SessionLocal, Base, engine
from fastapi.responses import RedirectResponse 


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

templates = Jinja2Templates(directory="templates")


Base.metadata.create_all(bind=engine)

@app.post("/home")
async def home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/register")
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

from fastapi import Form, HTTPException


@app.post("/register/")
async def register_user(
    # request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    # Check if the username already exists in the database
    existing_user = db.query(User).filter(User.username == username).first()
    if existing_user:
        # Username already exists, return an error message
        raise HTTPException(
            status_code=400,  # You can use an appropriate status code
            detail="Username already exists. Please choose a different username."
        )
    
    # If the username is not in use, proceed with registration
    user_data = {
        "username": username,
        "password": password,
        "is_active": True,
    }
    
    db_user = User(**user_data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    # Return a success message or render a confirmation page
    return RedirectResponse("/login")



@app.post("/login/")
async def login_user(
    # request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    db_user = db.query(User).filter(User.username == username).first()
    
    if not db_user:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username",
        )
    if db_user.password != password:
        raise HTTPException(
            status_code=400,
            detail="Incorrect password",
        )
    return RedirectResponse("/home")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
