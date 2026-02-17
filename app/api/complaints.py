from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.complaint import Complaint
from app.models.bus import Bus
from app.models.user import User
from app.schemas.complaint import ComplaintCreate, ComplaintResponse
from app.core.dependencies import get_current_user, get_db

router = APIRouter()


@router.get("/", response_model=list[ComplaintResponse])
def list_complaints(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return db.query(Complaint).filter(
        Complaint.company_id == current_user.company_id
    ).all()


@router.post("/", response_model=ComplaintResponse)
def create_complaint(
    data: ComplaintCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    bus = db.query(Bus).filter(
        Bus.id == data.bus_id,
        Bus.company_id == current_user.company_id
    ).first()

    if not bus:
        raise HTTPException(
            status_code=404,
            detail="Bus not found or not in your company"
        )

    complaint = Complaint(
        company_id=current_user.company_id,
        bus_id=data.bus_id,
        name=data.name,
        phone=data.phone,
        description=data.description,
        status="new"
    )

    db.add(complaint)
    db.commit()
    db.refresh(complaint)

    return complaint
