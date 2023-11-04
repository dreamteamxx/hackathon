from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers
from sqlalchemy.ext.asyncio import AsyncSession

from app.deps.db import get_async_session
from app.models import User
from app.overrides.db import SQLAlchemyUserDB
from app.overrides.user_manager import UserManager
from app.overrides.verify import get_verify_router


class FastAPIUsersMod(FastAPIUsers):
    def get_verify_router(self, user_schema: User) -> APIRouter:
        """
        Return a router with e-mail verification routes.

        :param user_schema: Pydantic schema of a public user.
        """
        return get_verify_router(get_user_manager, user_schema)


def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDB(session, User)


def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
