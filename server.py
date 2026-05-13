from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# 存 todo 的列表（重启服务器会清空）
todos = []


# 拿到所有 todo
@app.get("/api/todos")
def get_todos():
    return todos


# 加一个新 todo
@app.post("/api/todos")
def add_todo(data: dict):
    todos.append(data["text"])
    return todos


# 删掉一个 todo
@app.delete("/api/todos/{index}")
def delete_todo(index: int):
    todos.pop(index)
    return todos


# 把 index.html 作为首页
app.mount("/", StaticFiles(directory=".", html=True), name="static")
