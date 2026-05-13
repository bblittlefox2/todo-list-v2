# 从 fastapi 库里导入 FastAPI 这个类
# 它是用来创建 web 服务器的工具
# 官方文档：https://fastapi.tiangolo.com/
from fastapi import FastAPI

# 从 fastapi 里导入 StaticFiles
# 用来让服务器能提供静态文件（比如 html、图片）
# 文档：https://fastapi.tiangolo.com/tutorial/static-files/
from fastapi.staticfiles import StaticFiles

# 创建一个 FastAPI 应用，名字叫 app
# 后面所有的接口都会挂在这个 app 上
app = FastAPI()

# 准备一个空列表，用来存放所有的 todo
# 注意：服务器重启之后这个列表就会被清空
todos = []


# @app.get(...) 表示：当有人用 GET 方法访问这个网址时，执行下面这个函数
# 这里的网址是 /api/todos
# HTTP 方法介绍：https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Methods
@app.get("/api/todos")
def get_todos():
    # 直接把存好的 todos 列表返回给前端
    # FastAPI 会自动把它转成 JSON 格式
    return todos


# @app.post(...) 表示：当有人用 POST 方法访问 /api/todos 时，执行下面这个函数
# POST 一般用来「新建」东西
@app.post("/api/todos")
def add_todo(data: dict):
    # data 是前端发过来的数据，长这样：{"text": "买牛奶"}
    # 我们取出里面的 text 字段，加到 todos 列表后面
    todos.append(data["text"])
    # 返回最新的 todos 列表给前端
    return todos


# @app.delete(...) 表示：当有人用 DELETE 方法访问时，执行下面这个函数
# {index} 是一个占位符，访问时填的数字会被当作参数传给函数
# 路径参数文档：https://fastapi.tiangolo.com/tutorial/path-params/
@app.delete("/api/todos/{index}")
def delete_todo(index: int):
    # 根据 index 删掉 todos 里对应位置的那条
    # 比如 todos.pop(0) 会删掉第一条
    todos.pop(index)
    # 返回删除后的列表给前端
    return todos


# 把当前文件夹（.）作为静态文件目录，挂在 / 这个网址上
# html=True 表示访问 / 时自动返回 index.html
# 这样浏览器打开根网址就能看到 todo 页面
app.mount("/", StaticFiles(directory=".", html=True), name="static")
