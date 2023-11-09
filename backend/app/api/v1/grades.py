import logging
from typing import Any, Annotated, List

from fastapi.params import Depends
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio.session import AsyncSession
from starlette.responses import Response

from app.deps.db import get_async_session
from app.repositories.grade import GradeRepo
from app.schemas import GradeRead, GradeCreate, GradeUpdate

from app.models import Grade

router = APIRouter(prefix="/grades")

logger = logging.getLogger(__name__)

SessionDB = Annotated[AsyncSession, Depends(get_async_session)]


@router.get("", response_model=List[GradeRead])
async def get_grades(
    response: Response,
    session: SessionDB,
    skip: int = 0,
    limit: int = 100,
) -> Any:
    grade_repo: GradeRepo = GradeRepo(session)
    grades = await grade_repo.get_grades()
    if not grades:
        logger.info(f"Grades not found")
        return []
    return grades


@router.post("", response_model=GradeRead)
async def create_grade(
        session: SessionDB,
        grade_in: GradeCreate,
) -> Any:
    grade = Grade(**grade_in.model_dump())
    grade_repo: GradeRepo = GradeRepo(session)
    grade = await grade_repo.create_grade(grade)
    logger.info(f"Grade created")
    return grade


@router.patch("/{grade_id}", response_model=GradeUpdate)
async def update_grade(
        grade_id: int,
        response: Response,
        session: SessionDB,
        grade: GradeCreate,
) -> Any:
    grade_repo: GradeRepo = GradeRepo(session)
    grade_object = GradeUpdate(**grade.model_dump())
    grade = await grade_repo.update_grade(grade_id, grade_object)

    logger.info(f"Grade updated")
    return grade


@router.delete("/{grade_id}")
async def delete_grade(
        grade_id: int,
        response: Response,
        session: SessionDB,
) -> Any:
    grade_repo: GradeRepo = GradeRepo(session)
    await grade_repo.delete_grade(grade_id)
    logger.info(f"Grade deleted")
