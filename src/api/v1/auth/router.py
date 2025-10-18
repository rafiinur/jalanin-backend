from fastapi import APIRouter
from .schemas import LoginRequest, RegisterRequest, LoginResponse
from .services import login_service, register_service, logout

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=LoginResponse)
def handle_login(request: LoginRequest):
    """
    Authenticate user with email and password.
    Returns access token, refresh token, and user information.
    """
    return login_service(request)

@router.post("/register")
def handle_register(request: RegisterRequest):
    """
    Register a new user account.
    """
    return register_service(request)

@router.post("/logout")
def handle_logout():
    """
    Logout current user and invalidate tokens.
    """
    return logout()     