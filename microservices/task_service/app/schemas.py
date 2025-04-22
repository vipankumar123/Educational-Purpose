from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str
    user_id: int

class Task(BaseModel):
    id: int
    title: str
    description: str
    user_id: int

    class Config:
        orm_mode = True
