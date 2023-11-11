from typing import Any

import redis
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.core.config import settings

async_engine = create_async_engine(
    str(settings.ASYNC_DATABASE_URL), pool_pre_ping=True, pool_size=20, future=True
)

async_session_maker = async_sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    id: Any


redis = redis.from_url(url="redis://redis", db=0, decode_responses=True)
