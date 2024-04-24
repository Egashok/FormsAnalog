import typing
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from services.UserService import UserService

UserRouter = APIRouter(
    prefix="/users", tags=["user"]
)

@UserRouter.get("/{id}")
async def get(id: int ):
    return UserService.getId(id)
