import logging

from sqlalchemy import select, update, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError

from app import models
from app.repositories.repo import SQLAlchemyRepo
from app.schemas import OfficeRead, OfficeUpdate, OfficeCreate

logger = logging.getLogger(__name__)


class OfficeRepo(SQLAlchemyRepo):
    async def get_offices(self) -> list[OfficeRead] | None:
        stmt = await self.session.scalars(select(models.Office))
        result = await stmt.all()
        return list(map(models.Office.to_dto, result)) if result else None

    async def create_office(self, office: OfficeCreate) -> None:
        stmt = insert(models.Office).values(**office.model_dump())
        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except Exception as e:
            logger.error(f"Error creating office: {e}")
            await self.session.rollback()

    async def update_office(self, office_id: int, office: OfficeUpdate) -> None:
        stmt = update(models.Office).where(models.Office.id == office_id).values(**office.model_dump())
        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except IntegrityError as e:
            logger.error(f"Error updating office: {e}")
            await self.session.rollback()

    async def delete_office(self,office_id: int) -> None:
        stmt = delete(models.Office).where(models.Office.id == office_id)
        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except IntegrityError as e:
            logger.error(f"Error deleting office: {e}")
            await self.session.rollback()
