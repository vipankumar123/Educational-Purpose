from unittest.util import _MAX_LENGTH
from fastapi import FastAPI, Path, Query
from enum import Enum
from typing import Union
from pydantic import BaseModel

class schema1(BaseModel):
    name:str
    Class:str
    roll_no:int



class Choice_Names(str, Enum):
    one = "one"
    two = "two"
    three = "three"


app = FastAPI()

@app.get("/hello")
async def root():
    return {"message": "Hello from vipan side.."}

@app.get("/hy")
async def vipan():
    return {"message": "hy, how are you!!!"}


@app.get("/item/{Item}")
def path_func(Item):
    var_name = {"path variable": Item}
    return (var_name)


@app.get("/query")
def query_func(name: Union[str, None]= None, roll_no: Union[str, None]= Query(default=None, min_length=3, max_length=4)):
    var_name = {"name": name, "roll no": roll_no}
    return (var_name)


@app.get("/models/{model_name}")
async def get_model(model_name: Choice_Names):
    if model_name.value == "one":
        return {"model_name": model_name, "message": "Calling One!!"}

    if model_name.value == "two":
        return {"model_name": model_name, "message": "Calling two!!"}

    return {"model_name": model_name, "message": "Calling three"}


#request body 
@app.post("/items/")
async def create_item(item: schema1):
    return item

















