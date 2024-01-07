from fastapi import FastAPI, Query
from typing import Annotated # Annotated is used to add metadata to your parameters

app = FastAPI()


# additional validation
# you can define a regular expression pattern that the parameter should match

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=10, min_length=2, pattern="^A")] = ...): # Ellipsis declares that the value is required
    result = {"items": [
        {"item_id": "Foo"},
        {"item_id": "Bar"}
    ]}
    if q:
        result.update({"q": q})
    return result

# alias parameters
@app.get("/products/")
async def read_products(q: Annotated[list[str] | None, Query(
    title="Query list of strings",
    description="Query string for the items to search in the database that have a good match",
    alias="item-query"
    )] = ["Ricardo", "Cepeda", "Raza"]):
    
    query_items = {"q": q}
    return query_items


