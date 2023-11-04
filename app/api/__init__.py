from fastapi import APIRouter

from app.api.v1 import grades

api_router = APIRouter()
api_router.include_router(grades.router, tags=["grades"])
