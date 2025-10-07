from fastapi import FastAPI
# from app.api.v1.endpoints import router

app = FastAPI(title="ML API with FastAPI and Supabase")

# app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}