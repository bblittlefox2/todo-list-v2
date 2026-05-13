# 从 fastapi 拿到工具，用来写后端
from fastapi import FastAPI

# 这个工具让服务器能把 html 文件发给浏览器
from fastapi.staticfiles import StaticFiles

# 创建一个 web 服务器，名字叫 app
app = FastAPI()

# 用一个空列表存所有 todo（服务器重启会清空）
todos = []


# 浏览器来拿列表时，把 todos 发回去
@app.get("/api/todos")
def get_todos():
    return todos


# 浏览器送一条新 todo 过来时，加到列表里
@app.post("/api/todos")
def add_todo(data: dict):
    # data 长这样 {"text": "买牛奶"}
    todos.append(data["text"])
    return todos


# 浏览器要删第 index 条时，把它从列表里去掉
@app.delete("/api/todos/{index}")
def delete_todo(index: int):
    todos.pop(index)
    return todos


# 让浏览器访问根网址时直接看到 index.html
app.mount("/", StaticFiles(directory=".", html=True), name="static")
