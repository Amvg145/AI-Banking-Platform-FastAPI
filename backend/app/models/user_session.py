from sqlalchemy import (Column, Integer, Boolean, ForeignKey, DateTime, func)
from datetime import datetime

from app.database.base import Base

class UserSession(Base):
    __tablename__ = "user_sessions"

    id = Column(
        Integer,
        primary_key=True
    )
    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )
    login_time = Column(
        DateTime,
        default=func.now()
    )
    last_activity = Column(
        DateTime,
        default=func.now()
    )
    is_active = Column(
        Boolean,
        default=True
    )