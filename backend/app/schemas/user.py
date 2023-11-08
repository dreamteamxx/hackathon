import uuid
from datetime import datetime
from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    name: str
    surname: str
    login: str
    phone: Optional[int] = None
    birth_date: datetime
    is_admin: bool
    is_editor: bool
    created: datetime
    updated: datetime


class UserCreate(schemas.BaseUserCreate):
    name: str
    surname: str
    login: str
    phone: Optional[int] = None
    birth_date: datetime


class UserUpdate(schemas.BaseUserUpdate):
    pass
