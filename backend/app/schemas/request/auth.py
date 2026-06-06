from pydantic import BaseModel, EmailStr


class AuthRegisterRequest(BaseModel):
    email: EmailStr
    password: str
