# Dockerfile 是「怎么打包应用」的说明书
# 完整指令列表：https://docs.docker.com/reference/dockerfile/

# FROM 表示基于哪个镜像开始
# python:3.12-slim 是一个已经装好 Python 3.12 的精简镜像
# 镜像主页：https://hub.docker.com/_/python
FROM python:3.12-slim

# WORKDIR 设置工作目录，后面的命令都在这个目录里执行
# 相当于 cd /app
WORKDIR /app

# COPY 把本地的所有文件复制到镜像里
# 第一个 . 是本地路径，第二个 . 是镜像里的路径（就是当前 WORKDIR）
COPY . .

# RUN 在构建镜像的时候执行一个命令
# 这里用 pip 安装 requirements.txt 里列出的依赖
RUN pip install -r requirements.txt

# CMD 是容器启动时执行的命令
# uvicorn 是 Python 的 web 服务器，启动 server.py 里的 app
# --host 0.0.0.0 让外部能访问；--port $PORT 用 Render 给的端口
# uvicorn 文档：https://www.uvicorn.org/
CMD uvicorn server:app --host 0.0.0.0 --port $PORT
