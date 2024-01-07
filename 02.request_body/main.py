from fastapi import FastAPI
from pydantic import BaseModel

# define data model
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price  + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# you can declare path parameters and request body at the same time
# @app.put("/items/{item_id}")
# async def create_new_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}

# declare body, path, and query parameters, all at the same time
@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q:str | None = None, ):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

