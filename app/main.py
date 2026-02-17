from fastapi import FastAPI
from app.api import router
from app.core.config import settings
from app.db.session import engine
from app.models.base import Base
from app.models import company, complaint

app = FastAPI(title="VCA API")

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"status": "ok"}