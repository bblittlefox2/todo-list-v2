# 一个装好了 Python 3.12 的环境
FROM python:3.12-slim

# 进到 /app 目录
WORKDIR /app

# 把本地文件全部复制进去
COPY . .

# 装依赖
RUN pip install -r requirements.txt

# 启动服务器
CMD uvicorn server:app --host 0.0.0.0 --port $PORT
