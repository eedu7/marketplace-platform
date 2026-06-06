from fastapi import APIRouter

from app.schemas.request.auth import AuthRegisterRequest

router = APIRouter()


@router.post("/register")
async def register(data: AuthRegisterRequest):
    pass
