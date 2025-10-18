
from ....database import supabase
from .schemas import LoginRequest, RegisterRequest, LoginResponse, UserBase
from .exceptions import (
    InvalidCredentialsException,
    UserAlreadyExistsException,
    SupabaseException,
    RegistrationFailedException
)

def login_service(request: LoginRequest):
    try:
        # Panggil Supabase untuk sign in
        response = supabase.auth.sign_in_with_password({
            "email": request.email,
            "password": request.password,
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

    except Exception as e:
        # Fallback jika error spesifik tidak diketahui
        if "invalid login credentials" in str(e).lower():
            raise InvalidCredentialsException()
        raise SupabaseException(detail=str(e))

def register_service(request: RegisterRequest):
    try:
        # Coba buat user baru di Supabase
        response = supabase.auth.sign_up({
            "email": request.email,
            "password": request.password,
            "options": {
                "data": {
                    "full_name": request.full_name,
                    "role": "user" # Atur role default
                }
            }
        })
        
        if not response.user:
            raise RegistrationFailedException()

        return {"message": "Registration successful. Please check your email to verify."}
    # except AuthApiError as e:
    #     if "user already registered" in str(e).lower():
    #         raise UserAlreadyExistsException()
    #     raise SupabaseException(detail=str(e))
    except Exception as e:
        if "user already registered" in str(e).lower():
            raise UserAlreadyExistsException()
        raise SupabaseException(detail=str(e))

def logout():
    # Logika untuk logout (misal: memanggil supabase.auth.sign_out())
    # ...
    try:
        response = supabase.auth.sign_out()
        if not response.user:
            raise SupabaseException(detail="Logout failed.")
    except Exception as e:
        raise SupabaseException(detail=str(e))
    
    return {"message": "Logout successful."}