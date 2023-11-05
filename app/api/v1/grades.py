import logging
from typing import Any, Annotated, List

from fastapi.params import Depends
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio.session import AsyncSession
from starlette.responses import Response

from app.deps.db import get_async_session
from app.repositories.grade import GradeRepo
from app.schemas import GradeRead, GradeCreate, GradeUpdate

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


@router.post("", response_model=GradeCreate)
async def create_grade(
        response: Response,
        session: SessionDB,
        grade: GradeCreate,
) -> Any:
    grade_repo: GradeRepo = GradeRepo(session)
    await grade_repo.create_grade(grade)
    logger.info(f"Grade created")


@router.put("", response_model=GradeUpdate)
async def update_grade(
        response: Response,
        session: SessionDB,
        grade: GradeUpdate,
) -> Any:
    grade_repo: GradeRepo = GradeRepo(session)
    await grade_repo.update_grade(grade)
    logger.info(f"Grade updated")
