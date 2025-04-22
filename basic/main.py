from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float


data_items = [{"a": "b"}, {"c": "d"}]

app1 = FastAPI()


@app1.post("/create-items/{int:id}")
async def create_item(item: Item):
    print(item)
    if item.price == 90:
        item.price = 100
    try:
        if item.price is None:
            raise HTTPException(status_code=400, detail="price is required for creating this item!")
        return item
    except:
        raise HTTPException(status_code=400, detail="price is required for creating this item!")


@app1.get("/get-items/")
async def get_items():
    return data_items

