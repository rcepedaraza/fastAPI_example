from fastapi import FastAPI
from pydantic import BaseModel

from models.model_names import ModelName
from databases.music_db import music_genres


# create a FastAPI instance
app = FastAPI()


# create an endpoint or route operation(GET, POST, PUT, DELETE)
# define a path operation decorator
@app.get("/")
async def root(): #path operation function
    return {"message": "Hello World!"}


# path parameters

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# predefined values with enums
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    elif model_name == ModelName.lenet.value:
        return {"model_name": model_name, "message": "LeCNN all the images"}
    else:
        return {"model_name": model_name, "message": "Residual neural network"}
        
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

# query parameters
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return music_genres[skip : skip + limit]

# declare optional query parameters by setting their default to None
@app.get("/items/{item_id}")
async def read_items(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has an extra long description"}
        )
    return item

# multiple path and query parameters
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {
        "item_id": item_id, 
        "owner_id": user_id
        }
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "Finally, I got my car back!"})
    return item
