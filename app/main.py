from fastapi import FastAPI
from app.routes import router as items_router

app = FastAPI(title="MyShoppingDemo API", version="1.0.0")

app.include_router(items_router, prefix="/items", tags=["items"])

@app.get("/healthz", tags=["health"])
def health_check():
    return {"status": "ok"}
