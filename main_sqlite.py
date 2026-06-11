from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

conn = sqlite3.connect("items.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL
)
""")

conn.commit()
conn.close()


class Item(BaseModel):
    name: str
    price: float

@app.get("/items")
def get_items():
    conn = sqlite3.connect("items.db")  
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM items")
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.post("/items")
def post_item(item: Item):
    conn = sqlite3.connect("items.db")  
    cursor = conn.cursor() 
    cursor.execute("INSERT INTO items (name, price) VALUES (?, ?)", (item.name, item.price))
    conn.commit()
    conn.close()
    return "Item posted Succesfully"

@app.delete("/items/{item_id}")
def delete(item_id: int):
    conn = sqlite3.connect("items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM items WHERE id = ?", (item_id, ))
    item = cursor.fetchone()
    if item is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Item not found")
    cursor.execute("""DELETE FROM items WHERE id = ?""", (item_id,))
    conn.commit()
    conn.close()
    return f"item {item_id} deleted succesfully"

@app.put("/items/{item_id}")
def put(item_id: int, item: Item):
    conn = sqlite3.connect("items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM items WHERE id = ?", (item_id, ))
    item = cursor.fetchone()
    if item is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Item not found")
    cursor.execute("UPDATE items SET name = ?, price = ? WHERE id = ?", (item.name, item.price, item_id, ))
    conn.commit()
    conn.close()
    return f"Item {item_id} updated sucessfully"

