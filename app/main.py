from fastapi import FastAPI
from app.routers.orders import router as order_router

app = FastAPI()

app.include_router(order_router)


@app.get("/")
def home():
    return {"message": "dou+ agent 后端服务已启动"}