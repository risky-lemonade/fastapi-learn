# fastapi-learn

Learning FastAPI from scratch — routes, request handling, data validation, and database integration.

---

## main.py

Basic FastAPI app using in-memory storage (a Python list).

**Covers:**
- GET, POST, DELETE, PUT routes
- Path parameters and query parameters
- Pydantic models for request body validation
- In-memory CRUD operations with a list

**Run:**
```
uvicorn main:app --reload
```

---

## main_sqlite.py

Extended version of the app using a real SQLite database instead of in-memory storage.

**Covers:**
- SQLite integration with Python's built-in `sqlite3` module
- Persistent storage — data survives server restarts
- Table creation at startup with `CREATE TABLE IF NOT EXISTS`
- Parameterised queries with `?` placeholders to prevent SQL injection
- 404 error handling using `fetchone()` to check if a record exists before DELETE or UPDATE

**Run:**
```
uvicorn main_sqlite:app --reload
```

---

## Stack

- Python
- FastAPI
- SQLite
- Pydantic
- Uvicorn
