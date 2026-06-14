from sqlalchemy import (Column, Integer, String, DateTime, Float, ForeignKey, func)
from datetime import datetime
from app.database.base import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    account_id = Column(
        Integer,
        ForeignKey("accounts.id"),
        nullable=False
    )
    transaction_type = Column(
        String,
        nullable=False
    )
    amount = Column(
        Float,
        nullable=False
    )
    balance_after_transaction = Column(
        Float,
        nullable=False
    )
    description = Column(
        String
    )
    created_at = Column(
        DateTime,
        default=func.now()
    )