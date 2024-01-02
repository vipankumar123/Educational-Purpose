from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Optional
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from fastapi import WebSocket
from typing import List
from fastapi.templating import Jinja2Templates
from fastapi import WebSocket, WebSocketDisconnect
from fastapi.responses import RedirectResponse



DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    age = Column(Integer)
    hashed_password = Column(String)

from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    name: str
    age: int


# Use the Base class to create tables in the database
Base.metadata.create_all(bind=engine)

# Create a function that returns a SessionLocal class
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/register")
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register")
async def register_page(request: Request, username: str = Form(...), email: str = Form(...), name: str = Form(...), age: int = Form(...), password: str = Form(...)):
    db_user = User(username=username, email=email, name=name, age=age, hashed_password=password)
    db = SessionLocal()
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return templates.TemplateResponse("login.html", {"request": request, "message": "Registration successful"})

from fastapi import Request, Cookie

@app.get("/chat", response_class=HTMLResponse)
async def read_item(request: Request, user_id: int = Cookie(None)):
    return templates.TemplateResponse("chat.html", {"request": request, "user_id": user_id})


@app.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login_page(request: Request, username: str = Form(...), password: str = Form(...)):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        return templates.TemplateResponse("login.html", {"request": request, "message": "Incorrect username or password"})

    if user.hashed_password != password:
        return templates.TemplateResponse("login.html", {"request": request, "message": "Incorrect username or password"})

    # Store the user ID in the session
    response = RedirectResponse(url="/chat", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie("user_id", str(user.id))  # Store user ID in a cookie
    return response

class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"User {user_id}: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


















# from fastapi import FastAPI, WebSocket, Request
# from fastapi.templating import Jinja2Templates
# from fastapi.responses import HTMLResponse
# from fastapi.websockets import WebSocketDisconnect

# app = FastAPI()
# templates = Jinja2Templates(directory="templates")

# class ConnectionManager:
#     def __init__(self):
#         self.active_connections = []

#     async def connect(self, websocket: WebSocket):
#         await websocket.accept()
#         self.active_connections.append(websocket)

#     def disconnect(self, websocket: WebSocket):
#         self.active_connections.remove(websocket)

#     async def broadcast(self, message: str):
#         for connection in self.active_connections:
#             await connection.send_text(message)

# manager = ConnectionManager()

# @app.websocket("/ws/{client_id}")
# async def websocket_endpoint(websocket: WebSocket, client_id: int):
#     await manager.connect(websocket)
#     try:
#         while True:
#             data = await websocket.receive_text()
#             await manager.broadcast(f"Client {client_id}: {data}")
#     except WebSocketDisconnect:
#         manager.disconnect(websocket)

# @app.get("/chat", response_class=HTMLResponse)
# async def read_item(request: Request):
#     return templates.TemplateResponse("chat.html", {"request": request})
