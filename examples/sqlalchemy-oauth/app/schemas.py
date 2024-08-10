import uuid
from typing import Optional
from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    is_evaluator: bool = False


class UserCreate(schemas.BaseUserCreate):
    is_evaluator: bool = False


class UserUpdate(schemas.BaseUserUpdate):
    is_evaluator: Optional[bool] = False
