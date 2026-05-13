from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
todos = []

@app.get("/api/todos")
def list_todos(): return todos

@app.post("/api/todos")
def add(t: dict): todos.append(t["text"]); return todos

@app.delete("/api/todos/{i}")
def remove(i: int): todos.pop(i); return todos

app.mount("/", StaticFiles(directory=".", html=True), name="x")
