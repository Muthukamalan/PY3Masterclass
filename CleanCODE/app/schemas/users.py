from pydantic import BaseModel, field_validator
from typing import Optional, Sequence
from datetime import datetime


class UserCreate(BaseModel):
    name: str
    email: str

    @field_validator("email")
    @classmethod
    def validate_email(cls, v):
        if "@" not in v or "." not in v:
            raise ValueError("Invalid email format")
        return v

    class Config:
        str_strip_whitespace = True


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

    @field_validator("email")
    @classmethod
    def validate_email(cls, v):
        if v and ("@" not in v or "." not in v):
            raise ValueError("Invalid email format")
        return v

    class Config:
        str_strip_whitespace = True


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UserListResponse(BaseModel):
    data: Sequence[UserResponse]
    total: int

    class Config:
        from_attributes = True
