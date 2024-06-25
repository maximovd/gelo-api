from fastapi import FastAPI

from app.api.router import router

app = FastAPI()

app.include_router(router)
