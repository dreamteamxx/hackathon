import sentry_sdk
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles
from fastapi_users import FastAPIUsers
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import FileResponse
from starlette_exporter import PrometheusMiddleware, handle_metrics

from app.api import api_router
from app.core.config import settings
from app.deps.users import fastapi_users, jwt_authentication
from app.schemas.user import UserCreate, UserRead, UserUpdate


def create_app():
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        traces_sample_rate=1.0,
    )
    description = f"{settings.PROJECT_NAME} API"
    app = FastAPI(
        docs_url="/docs/",
    )

    def custom_openapi() -> dict:
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title="Ou loomin API",
            version="0.3.4b",
            routes=app.routes,
        )
        openapi_schema["info"]["x-logo"] = {
            "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
        }
        app.openapi_schema = openapi_schema
        return app.openapi_schema

    app.openapi = custom_openapi
    setup_routers(app, fastapi_users)
    setup_cors_middleware(app)
    serve_static_app(app)
    return app


def setup_routers(app: FastAPI, fastapi_users_class: FastAPIUsers) -> None:
    app.include_router(api_router, prefix=settings.API_PATH)
    app.include_router(
        fastapi_users_class.get_auth_router(
            jwt_authentication,
            requires_verification=False,
        ),
        prefix=f"{settings.API_PATH}/auth/jwt",
        tags=["auth"],
    )
    app.include_router(
        fastapi_users_class.get_verify_router(UserRead),
        prefix=f"{settings.API_PATH}/auth",
        tags=["auth"],
    )
    app.include_router(
        fastapi_users_class.get_register_router(UserRead, UserCreate),
        prefix=f"{settings.API_PATH}/auth",
        tags=["auth"],
    )
    app.include_router(
        fastapi_users_class.get_users_router(
            UserRead, UserUpdate, requires_verification=False
        ),
        prefix=f"{settings.API_PATH}/users",
        tags=["users"],
    )
    # The following operation needs to be at the end of this function
    use_route_names_as_operation_ids(app)
    app.add_middleware(PrometheusMiddleware)
    app.add_route("/metrics", handle_metrics)


def serve_static_app(app):
    app.mount("/", StaticFiles(directory="static"), name="static")

    @app.middleware("http")
    async def _add_404_middleware(request: Request, call_next):
        """Serves static assets on 404"""
        response = await call_next(request)
        path = request["path"]
        if path.startswith(settings.API_PATH) or path.startswith("/docs"):
            return response
        if response.status_code == 404:
            return FileResponse("static/index.html")
        return response


def setup_cors_middleware(app):
    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            expose_headers=["Content-Range", "Range"],
            allow_headers=["Authorization", "Range", "Content-Range"],
        )


def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    route_names = set()
    for route in app.routes:
        if isinstance(route, APIRoute):
            if route.name in route_names:
                raise Exception("Route function names should be unique")
            route.operation_id = route.name
            route_names.add(route.name)
