import uvicorn
from routers.UserRouter import UserRouter

from fastapi import FastAPI

app = FastAPI()


app.include_router(UserRouter)
