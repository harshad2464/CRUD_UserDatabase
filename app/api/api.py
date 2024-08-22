from fastapi import APIRouter
from app.api.endpoints import home
from app.api.endpoints import crud_api

api_router = APIRouter()

api_router.include_router(home.router, prefix="/home", tags=["home"])
api_router.include_router(crud_api.router, prefix="/crud_api", tags=["crud_api"])
