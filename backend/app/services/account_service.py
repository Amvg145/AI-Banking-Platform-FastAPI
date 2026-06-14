from sqlalchemy.orm import Session
from app.models.account import Account

def create_account(
        db: Session,
        user_id: int,
        account_type: str
):
    account_count = (
        db.query(Account).count()
    )

    account_number = (
        f"ACC{100000 + account_count + 1}"
    )

    account = Account(
        user_id=user_id,
        account_number=account_number,
        account_type=account_type,
        balance=0,
        status="ACTIVE"
    )

    db.add(account)
    db.commit()
    db.refresh(account)
    return account
