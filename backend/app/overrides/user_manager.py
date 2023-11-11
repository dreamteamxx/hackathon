import logging
import uuid
from typing import Optional

from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_users import UUIDIDMixin, BaseUserManager, schemas, models, exceptions
from starlette.requests import Request

from app.core.config import settings
from app.errors import consts
from app.models import User
from app.overrides.db import SQLAlchemyUserDB
from app.schemas.user import UserCreate

logger = logging.getLogger(__name__)


async def check_user_exists(user_create: UserCreate, user_db: SQLAlchemyUserDB) -> bool:
    if await user_db.get_by_username(user_create.login):
        raise HTTPException(
            status_code=400,
            detail=consts.USER_LOGIN_EXISTS,
        )
    if await user_db.get_by_email(user_create.email):
        raise HTTPException(
            status_code=400,
            detail=consts.USER_EMAIL_EXISTS,
        )
    if await user_db.get_by_phone(user_create.phone):
        raise HTTPException(
            status_code=400,
            detail=consts.USER_PHONE_EXISTS,
        )
    return True


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = settings.SECRET_KEY
    verification_token_secret = settings.SECRET_KEY

    # override create method to add user to database
    async def create(
        self,
        user_create: schemas.UC,
        safe: bool = False,
        request: Optional[Request] = None,
    ) -> models.UP:
        """
        Create a user in database.

        Triggers the on_after_register handler on success.

        :param user_create: The UserCreate model to create.
        :param safe: If True, sensitive values like is_superuser or is_verified
        will be ignored during the creation, defaults to False.
        :param request: Optional FastAPI request that
        triggered the operation, defaults to None.
        :raises UserAlreadyExists: A user already exists with the same e-mail.
        :return: A new user.
        """
        await self.validate_password(user_create.password, user_create)

        self.user_db: SQLAlchemyUserDB
        if not await check_user_exists(user_create, self.user_db):
            raise exceptions.UserAlreadyExists()

        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )
        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)

        created_user = await self.user_db.create(user_dict)
        if created_user is None:
            raise exceptions.UserAlreadyExists()

        await self.on_after_register(created_user, request)

        return created_user

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        logger.info(f"User {user.id} has registered.")
        await self.request_verify(user, request)

    async def authenticate(
        self, credentials: OAuth2PasswordRequestForm
    ) -> Optional[models.UP]:
        self.user_db: SQLAlchemyUserDB
        try:
            user = await self.user_db.get_by_username(credentials.username)
        except exceptions.UserNotExists:
            # Run the hasher to mitigate timing attack
            # Inspired from Django: https://code.djangoproject.com/ticket/20760
            self.password_helper.hash(credentials.password)
            return None

        verified, updated_password_hash = self.password_helper.verify_and_update(
            credentials.password, user.hashed_password
        )
        if not verified:
            return None
        # Update password hash to a more robust one if needed
        if updated_password_hash is not None:
            await self.user_db.update(user, {"hashed_password": updated_password_hash})

        return user
