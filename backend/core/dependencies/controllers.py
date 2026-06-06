from typing import Annotated

from fastapi import Depends

from app.controllers import AuthController, UserController
from core.factory import Factory

UserControllerDep = Annotated[UserController, Depends(Factory.get_user_controller)]
AuthControllerDep = Annotated[AuthController, Depends(Factory.get_auth_controller)]
