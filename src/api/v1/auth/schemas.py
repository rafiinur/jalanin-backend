from pydantic import BaseModel, EmailStr, Field, field_validator
from enum import Enum
from typing import Optional

class Role (str, Enum):
    ADMIN = "admin"
    USER = "user"

class UserBase(BaseModel):
    id: str
    email: str
    full_name: str
    role: Role
    avatar_url: Optional[str] = None
    created_at: Optional[str] = None

class LoginRequest(BaseModel):
    # Pydantic akan otomatis memvalidasi format email
    email: EmailStr 
    password: str = Field(
        ..., 
        min_length=8, 
        description="Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character."
    )

class RegisterRequest(BaseModel):
    email: EmailStr 
    password: str = Field(
        ..., 
        min_length=8, 
        description="Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character."
    )
    full_name: str


class LoginResponse(BaseModel):
    user: UserBase
    access_token: str
    refresh_token: str

