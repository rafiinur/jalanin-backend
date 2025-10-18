from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from src.database import supabase 
from .exceptions import InvalidTokenException 
from .schemas import UserBase 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)) -> UserBase:
    """
    Dependency to get the current authenticated user based on the provided token.
    """
    try:
        response = supabase.auth.get_user(token)
        user = response.user
        
        return UserBase(
            id=user.id,
            email=user.email,
            full_name=user.user_metadata.get("full_name", ""),
            role=user.user_metadata.get("role", "user"),
            avatar_url=user.user_metadata.get("avatar_url"),
            created_at=str(user.created_at)
        )
    except Exception:
        raise InvalidTokenException()