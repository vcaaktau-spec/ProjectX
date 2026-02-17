from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.models.base import Base
import datetime


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    bin = Column(String, index=True)
    city = Column(String)
    logo = Column(String)
    brand_color = Column(String)
    subscription_plan = Column(String)
    subscription_expiry = Column(DateTime)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    users = relationship("User", back_populates="company")
    buses = relationship("Bus", back_populates="company")
    complaints = relationship("Complaint", back_populates="company")