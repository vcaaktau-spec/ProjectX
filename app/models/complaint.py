from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base
import datetime


class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)

    company_id = Column(Integer, ForeignKey("companies.id", ondelete="CASCADE"), nullable=False, index=True)
    bus_id = Column(Integer, ForeignKey("buses.id", ondelete="CASCADE"), nullable=False, index=True)

    name = Column(String)
    phone = Column(String)
    description = Column(String)
    media_path = Column(String)

    status = Column(String, default="new", index=True)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    company = relationship("Company", back_populates="complaints")
    bus = relationship("Bus", back_populates="complaints")