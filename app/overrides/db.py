import logging
import uuid
from typing import Optional

from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy import select, update
from sqlalchemy.exc import IntegrityError

from app.models import User

logger = logging.getLogger(__name__)


class SQLAlchemyUserDB(SQLAlchemyUserDatabase[User, uuid.UUID]):
    async def save_telegram_auth_token(self, token, user: User):
        logger.info(f"Saving verification token for user {user.id}.")
        user.verify_token = token
        await self.session.commit()
        return token

    async def get_by_verify_token(self, token: str) -> Optional[User]:
        logger.info(f"Getting user by verification token.")
        user = await self.session.execute(
            select(User).where(User.verify_token == token)
        )
        return user.scalars().first()

    async def verify_user(self, user: User, telegram_id: int) -> User:
        await self.session.execute(
            update(User)
            .where(User.id == user.id)
            .values(verify_token=None, is_verified=True, telegram_id=telegram_id)
        )
        await self.session.commit()
        return await self.get(user.id)

    async def get_by_username(self, username: str) -> Optional[User]:
        logger.info(f"Getting user by username {username}")
        user = await self.session.scalars(select(User).where(User.login == username))
        return user.first()

    async def create(self, create_dict: dict) -> User | None:
        user = User(**create_dict)
        self.session.add(user)
        try:
            await self.session.commit()
        except IntegrityError as e:
            logger.error(f"Error creating user: {e.detail} with data {create_dict}")
            return None
        await self.session.refresh(user)
        return user

    async def get_by_phone(self, phone: int) -> Optional[User]:
        logger.info(f"Getting user by phone {phone}")
        user = await self.session.scalars(select(User).where(User.phone == phone))
        return user.first()
