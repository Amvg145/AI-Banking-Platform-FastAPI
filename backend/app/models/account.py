from sqlalchemy import (Column, Integer, String, DateTime, Float, ForeignKey)
from sqlalchemy.sql import func

from app.database.base import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(
        Integer, 
        primary_key=True, 
        index=True
    )
    user_id = Column(
        Integer, 
        ForeignKey("users.id")
    )
    account_number = Column(
        String, 
        unique=True
    )
    account_type = Column(
        String, 
        default="SAVINGS"
    )
    balance = Column(
        Float, 
        default=0
    )
    status = Column(
        String,
        default="ACTIVE"
    )
    created_at = Column(
        DateTime,
        default=func.now()
    )
