from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base
import datetime


class Bus(Base):
    __tablename__ = "buses"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id", ondelete="CASCADE"), nullable=False, index=True)

    bus_number = Column(String, nullable=False, index=True)
    route = Column(String, nullable=False, index=True)
    status = Column(String, default="active")

    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    company = relationship("Company", back_populates="buses")
    complaints = relationship("Complaint", back_populates="bus")