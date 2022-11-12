from unittest.util import _MAX_LENGTH
from fastapi import FastAPI, Query, Form, File, UploadFile, HTTPException
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

# First Fastapi function
@app.get("/hello")
async def root():
    return {"message": "Hello from vipan side.."}

@app.get("/hy")
async def vipan():
    return {"message": "hy, how are you!!!"}


# Path parameters
@app.get("/item/{Item}")
def path_func(Item):
    var_name = {"path variable": Item}
    return (var_name)

# Query parameters
@app.get("/query")
def query_func(name: Union[str, None]= None, roll_no: Union[str, None]= Query(default=None, min_length=3, max_length=4)):
    var_name = {"name": name, "roll no": roll_no}
    return (var_name)

# Choice field
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


class vipan(BaseModel):
    one : str
    two : str
    three : int

# form data
@app.post("/form/data")
async def form_data(username : str = Form(), passowrd : str = Form()):
    return ({"username": username, "password": passowrd})

# file upload
@app.post("/file/upload")
async def file_bytes_len(file : bytes = File()):
    return ({"file": len(file)})


@app.post("/upload/file")
async def file_upload(file : UploadFile):
    return ({"file_name": file.filename, "file_content_name": file.content_type})


@app.post("/form/data/filedata")
async def formdata_uploadfile(file1 : UploadFile, file2: bytes = File(), name: str = Form()):
    return ({"file_name": file1.filename, "file2_bytes": len(file2), "name": name})


items = [1,2,3,4,5]


# error handling
@app.get("/error/handling")
async def handle_error(item: int):
    if item not in items:
        return HTTPException(status_code= 400, detail="Item is not eqal to 2 try another value!!!")
    return {"value": item}



class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

# Declare request example data.
    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results






