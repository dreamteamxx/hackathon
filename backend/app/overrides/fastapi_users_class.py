from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers
from sqlalchemy.ext.asyncio import AsyncSession

from app.deps.db import get_async_session
from app.models import User
from app.overrides.db import SQLAlchemyUserDB
from app.overrides.user_manager import UserManager


class FastAPIUsersMod(FastAPIUsers):
    ...


def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDB(session, User)


def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
