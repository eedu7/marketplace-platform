from fastapi import APIRouter

from app.schemas.request.auth import AuthRegisterRequest
from core.dependencies.controllers import AuthControllerDep

router = APIRouter()


@router.post("/register")
async def register(data: AuthRegisterRequest, controller: AuthControllerDep):
    return await controller.register(**data.model_dump())
