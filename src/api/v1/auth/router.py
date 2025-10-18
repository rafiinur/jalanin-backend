from fastapi import APIRouter, Depends 
from fastapi.security import OAuth2PasswordRequestForm
from .schemas import RegisterRequest, LoginResponse, UserBase
from .services import authenticate_user, register_user
from .dependencies import get_current_user 

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=LoginResponse)
def handle_login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Authenticate user.
    FastAPI akan secara otomatis mengambil `username` dan `password` dari form body.
    """
    # Panggil service dengan data dari form
    # Perhatikan: form_data.username berisi email yang dikirim pengguna
    return authenticate_user(email=form_data.username, password=form_data.password)

@router.post("/register")
def handle_register(request: RegisterRequest):
    return register_user(request)

@router.get("/user", response_model=UserBase)
def get_user_data(current_user: UserBase = Depends(get_current_user)):
    """
    Mengambil informasi user yang sedang login.
    Endpoint ini sekarang terproteksi. Hanya request dengan token valid yang bisa mengaksesnya.
    """
    return current_user