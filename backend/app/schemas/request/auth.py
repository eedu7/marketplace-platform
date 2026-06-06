from pydantic import BaseModel, EmailStr


class AuthRegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
