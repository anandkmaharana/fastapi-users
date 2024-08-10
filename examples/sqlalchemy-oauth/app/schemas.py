import uuid
from typing import Optional
from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    first_name: str
    last_name: str
    is_evaluator: bool = False


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    last_name: str
    is_evaluator: bool = False


class UserUpdate(schemas.BaseUserUpdate):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_evaluator: Optional[bool] = False
