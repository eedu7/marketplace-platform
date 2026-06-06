from pydantic import EmailStr

from app.models import DBUser
from app.repositories import UserRepository
from core.controller import BaseController


class AuthController(BaseController[DBUser]):
    def __init__(self, repository: UserRepository) -> None:
        super().__init__(DBUser, repository)
        self.repository = repository

    async def register(self, email: EmailStr, password: str) -> DBUser:
        return await self.repository.create({"email": str(email), "password": password})
