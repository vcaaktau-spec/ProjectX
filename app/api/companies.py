from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.company import Company
from app.models.user import User
from app.schemas.company import CompanyResponse
from app.core.dependencies import get_current_user, get_db

router = APIRouter()


@router.get("/", response_model=list[CompanyResponse])
def list_companies(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(Company).filter(
        Company.id == current_user.company_id
    ).all()
