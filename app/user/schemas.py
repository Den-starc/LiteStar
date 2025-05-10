from pydantic import BaseModel
from datetime import datetime


class UserCreate(BaseModel):
    name: str
    surname: str
    password: str


class UserRead(UserCreate):
    id: int
    created_at: datetime
    updated_at: datetime


class UserUpdate(BaseModel):
    name: str | None = None
    surname: str | None = None
    password: str | None = None
