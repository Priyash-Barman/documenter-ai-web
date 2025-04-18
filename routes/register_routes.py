from fastapi import FastAPI

from api import user_api, auth_api


def register_routes(app: FastAPI):
    app.include_router(user_api.router, prefix="/users", tags=["Users"])
    app.include_router(auth_api.router, prefix="/auth", tags=["Auth"])
