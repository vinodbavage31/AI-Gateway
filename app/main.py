from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="AI Gateway Service")       # Creates ASGI application

app.include_router(router)                      # Mounts routes

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/")
async def root():
    return {"message": "AI Gateway Running"}