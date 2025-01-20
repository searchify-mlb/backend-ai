from pydantic import BaseModel, EmailStr
from datetime import datetime
import uuid
from typing import Optional

class UserBaseSchema(BaseModel):
    email: EmailStr

class UserCreateSchema(UserBaseSchema):
    password: str

class UserReadSchema(UserBaseSchema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

class UserUpdateSchema(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None

class LoginRequest(BaseModel):
    email: str
    password: str
