from fastapi import FastAPI
from src.api.v1.auth.router import router as auth_router
from src.api.v1.destinations.router import router as destinations_router

app = FastAPI(title="Jalanin")

# Include all routers with /api/v1 prefix
app.include_router(auth_router, prefix="/api/v1")
app.include_router(destinations_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}

