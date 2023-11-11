import logging

import redis.asyncio
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
    RedisStrategy,
)

from app.core.config import settings
from app.overrides.fastapi_users_class import FastAPIUsersMod, get_user_manager

logger = logging.getLogger(__name__)

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

redis = redis.asyncio.from_url(url="redis://redis", db=0, decode_responses=True)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=settings.SECRET_KEY,
        lifetime_seconds=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    )


def get_redis_strategy() -> RedisStrategy:
    return RedisStrategy(
        redis, lifetime_seconds=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
    )


jwt_authentication = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
#
# redis_authentication = AuthenticationBackend(
#     name="redis",
#     transport=bearer_transport,
#     get_strategy=get_redis_strategy,
# )


fastapi_users = FastAPIUsersMod(get_user_manager, [jwt_authentication])

current_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)
verified_user = fastapi_users.current_user(active=True, verified=True)
