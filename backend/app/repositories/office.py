import logging

from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from app import models
from app.models import Office
from app.repositories.repo import SQLAlchemyRepo
from app.schemas import OfficeRead, OfficeUpdate

logger = logging.getLogger(__name__)


class OfficeRepo(SQLAlchemyRepo):
    async def get_offices(self) -> list[OfficeRead] | None:
        stmt = await self.session.scalars(select(models.Office))
        result = stmt.all()
        return list(map(models.Office.to_dto, result)) if result else None

    async def create_office(self, office: Office) -> Office:
        try:
            self.session.add(office)
            await self.session.commit()
            return office
        except Exception as e:
            logger.error(f"Error creating office: {e}")
            await self.session.rollback()

    async def update_office(self, office_id: int, office: OfficeUpdate) -> OfficeUpdate:
        stmt = update(Office).where(Office.id == office_id).values(**office.model_dump())
        await self.session.execute(stmt)
        await self.session.commit()
        return office

    async def delete_office(self, office_id: int) -> None:
        stmt = delete(models.Office).where(models.Office.id == office_id)
        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except IntegrityError as e:
            logger.error(f"Error deleting office: {e}")
            await self.session.rollback()
