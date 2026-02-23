from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="AI Gateway Service")

app.include_router(router)

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/")
async def root():
    return {"message": "AI Gateway Running"}