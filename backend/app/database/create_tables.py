from app.database.db import engine
from app.database.base import Base
from app.models.user import User
from app.models.account import Account
from app.models.transaction import Transaction
from app.models.user_session import UserSession

Base.metadata.create_all(bind=engine)

print("Tables created Successfully")