
from src.database import supabase
from .schemas import RegisterRequest, LoginResponse, UserBase
from .exceptions import (
    InvalidCredentialsException,
    UserAlreadyExistsException,
    SupabaseException,
    RegistrationFailedException
)
from utils import validate_email, validate_password_strength
from constants import DEFAULT_USER_ROLE

def authenticate_user(email: str, password: str) -> LoginResponse:
    if not validate_email(email):
        raise InvalidCredentialsException()
    if not validate_password_strength(password):
        raise InvalidCredentialsException()
    
    try:
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password,
        })
        
        user_data = UserBase(
            id=response.user.id,
            email=response.user.email,
            full_name=response.user.user_metadata.get("full_name", ""),
            role=response.user.user_metadata.get("role", "user"),
            avatar_url=response.user.user_metadata.get("avatar_url"),
            created_at=str(response.user.created_at)
        )

        return LoginResponse(
            user=user_data,
            access_token=response.session.access_token,
            refresh_token=response.session.refresh_token,
        )
    except Exception:
        raise InvalidCredentialsException()
    
def register_user(request: RegisterRequest):
    try:
        response = supabase.auth.sign_up({
            "email": request.email,
            "password": request.password,
            "options": {
                "data": {
                    "full_name": request.full_name,
                    "role": DEFAULT_USER_ROLE
                }
            }
        })
        
        if not response.user:
            raise RegistrationFailedException()

        return {"message": "Registration successful. Please check your email to verify."}
    except Exception as e:
        if "user already registered" in str(e).lower():
            raise UserAlreadyExistsException()
        raise SupabaseException(detail=str(e))
