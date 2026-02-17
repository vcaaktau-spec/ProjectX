from fastapi import APIRouter

from app.api import companies, complaints, auth

router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["Auth"])
router.include_router(companies.router, prefix="/companies", tags=["Companies"])
router.include_router(complaints.router, prefix="/complaints", tags=["Complaints"])
