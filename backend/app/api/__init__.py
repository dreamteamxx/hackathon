from fastapi import APIRouter

from app.api.v1 import grades, employee_reference, offices, task_distributions, task_reference

api_router = APIRouter()
api_router.include_router(grades.router, tags=["grades"])
api_router.include_router(employee_reference.router, tags=["employee_reference"])
api_router.include_router(offices.router, tags=["offices"])
api_router.include_router(task_distributions.router, tags=["task_distribution"])
api_router.include_router(task_reference.router, tags=["task_reference"])
