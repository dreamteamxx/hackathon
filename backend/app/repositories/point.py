import logging

from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from app import models
from app.models import Point
from app.repositories.repo import SQLAlchemyRepo
from app.schemas import PointUpdate, PointRead

logger = logging.getLogger(__name__)


class PointRepo(SQLAlchemyRepo):
    async def get_point(self, point_id: int) -> PointRead:
        query = await self.session.execute(
            select(models.Point).where(models.Point.id == point_id)
        )
        result = query.scalars().first()
        return result.to_dto() if result else None

    async def get_points(self) -> list[PointRead] | None:
        stmt = await self.session.scalars(select(models.Point))
        result = stmt.all()
        return list(map(models.Point.to_dto, result)) if result else None

    async def create_point(self, point: Point) -> Point:
        try:
            self.session.add(point)
            await self.session.commit()
            return point

        except Exception as e:
            logger.error(f"Error creating point: {e}")
            await self.session.rollback()

    async def update_point(self, point_id: int, point_new: PointUpdate) -> PointUpdate:
        stmt = update(Point).where(Point.id == point_id).values(**point_new.model_dump())
        await self.session.execute(stmt)
        await self.session.commit()
        return point_new

    async def delete_point(self, point_id: int) -> None:
        stmt = delete(models.Point).where(models.Point.id == point_id)
        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except IntegrityError as e:
            logger.error(f"Error deleting point: {e}")
            await self.session.rollback()
