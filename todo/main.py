# main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, database
import crud
import schema

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Dependency to get database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Todo
@app.post("/todos/", response_model=schema.Todoo)
def create_todo(todo: schema.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)

# Get Todo by ID
@app.get("/todos/{todo_id}", response_model=schema.Todoo)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

# Update Todo
@app.put("/todos/{todo_id}", response_model=schema.Todoo)
def update_todo(todo_id: int, todo: schema.TodoCreate, db: Session = Depends(get_db)):
    db_todo = crud.update_todo(db, todo_id, todo)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

# Delete Todo
@app.delete("/todos/{todo_id}", response_model=schema.Todoo)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.delete_todo(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

# Get All Todos
@app.get("/todos/", response_model=list[schema.Todoo])
def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_todos(db, skip=skip, limit=limit)
