from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
class Item(BaseModel):
    name: str
    price: int
items_db = []

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Hello, World!"}
@app.get("/about")
def about():
    return{"app": "FastAPI Learn", "version": "1.0"}
@app.get("/user/{name}")
def user(name):
    return {"message": f"Hello, {name}"}
@app.get("/search")
def search(q):
    return {"you searched for" : f"{q}"}
@app.get("/product")
def product(name:str, price:int):
    return {"product": name, "price": price}
@app.get("/greet")
def greet(name: str, lang: str = "en"):
    if lang == "hi":
        return {"message": f"Namaste, {name}"}

    return {"message": f"Hello, {name}"}




@app.post("/items")
def items(item: Item):
    items_db.append(item)
    return {"message": "Item added", "item": item}

@app.get("/items")
def get_items():
    return items_db


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    deleted_item = items_db.pop(item_id)

    return {
        "message": "Item deleted",
        "item": deleted_item
    }


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    items_db[item_id] = item.model_dump()

    return {
        "message": "Item updated",
        "item": items_db[item_id]
    }