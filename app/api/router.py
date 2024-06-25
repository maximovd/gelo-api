from fastapi import APIRouter

from app.api.gelo.v1 import router as gelo_router

router = APIRouter()

router.include_router(gelo_router.router, prefix="/v1/gelo", tags=["gelo"])
