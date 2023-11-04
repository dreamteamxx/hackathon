import logging

from fastapi import APIRouter, Body, Depends, HTTPException, Request, status
from fastapi_users import exceptions, models
from fastapi_users.manager import UserManagerDependency
from fastapi_users.router.common import ErrorCode, ErrorModel
from pydantic import EmailStr

from app.models import User
from app.overrides.user_manager import UserManager
from app.schemas.msg import VerifyToken, TelegramVerify

logger = logging.getLogger(__name__)


def get_verify_router(
    get_user_manager: UserManagerDependency[models.UP, models.ID],
    user_schema: User,
):
    router = APIRouter()

    @router.post(
        "/request-verify-token",
        status_code=status.HTTP_202_ACCEPTED,
        name="verify:request-token",
        response_model=VerifyToken,
        responses={
            status.HTTP_400_BAD_REQUEST: {
                "model": ErrorModel,
                "content": {
                    "application/json": {
                        "examples": {
                            ErrorCode.VERIFY_USER_BAD_TOKEN: {
                                "summary": "Bad token, not existing user or"
                                "not the e-mail currently set for the user.",
                                "value": {"detail": ErrorCode.VERIFY_USER_BAD_TOKEN},
                            },
                            ErrorCode.VERIFY_USER_ALREADY_VERIFIED: {
                                "summary": "The user is already verified.",
                                "value": {
                                    "detail": ErrorCode.VERIFY_USER_ALREADY_VERIFIED
                                },
                            },
                        }
                    }
                },
            }
        },
    )
    async def request_verify_token(
        request: Request,
        email: EmailStr = Body(..., embed=True),
        user_manager: UserManager = Depends(get_user_manager),
    ):
        try:
            user = await user_manager.get_by_email(email)
            verify_token = await user_manager.request_verify(user, request)
            return verify_token
        except exceptions.UserNotExists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorCode.VERIFY_USER_BAD_TOKEN,
            )
        except exceptions.UserAlreadyVerified:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorCode.VERIFY_USER_ALREADY_VERIFIED,
            )
        except exceptions.UserInactive:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="USER_INACTIVE"
            )

    @router.post(
        "/verify",
        response_model=user_schema,
        name="verify:verify",
        responses={
            status.HTTP_400_BAD_REQUEST: {
                "model": ErrorModel,
                "content": {
                    "application/json": {
                        "examples": {
                            ErrorCode.VERIFY_USER_BAD_TOKEN: {
                                "summary": "Bad token, not existing user or"
                                "not the e-mail currently set for the user.",
                                "value": {"detail": ErrorCode.VERIFY_USER_BAD_TOKEN},
                            },
                            ErrorCode.VERIFY_USER_ALREADY_VERIFIED: {
                                "summary": "The user is already verified.",
                                "value": {
                                    "detail": ErrorCode.VERIFY_USER_ALREADY_VERIFIED
                                },
                            },
                        }
                    }
                },
            }
        },
    )
    async def verify(
        request: Request,
        user_verify: TelegramVerify,
        user_manager: UserManager = Depends(get_user_manager),
    ):
        try:
            user = await user_manager.verify(user_verify, request)
            return user
        except (exceptions.InvalidVerifyToken, exceptions.UserNotExists):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorCode.VERIFY_USER_BAD_TOKEN,
            )
        except exceptions.UserAlreadyVerified:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorCode.VERIFY_USER_ALREADY_VERIFIED,
            )

    return router
