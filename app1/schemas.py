from typing import List, Union
from pydantic import BaseModel
from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    # if not description, then default None value added
    description: Union[str, None] = None 


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    is_active: bool
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
