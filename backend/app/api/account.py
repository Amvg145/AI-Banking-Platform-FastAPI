from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database.db import get_db

from app.schemas.account_schema import AccountCreate, AccountResponse
from app.services.account_service import create_account
from app.schemas.transaction_schema import WithdrawRequest, DepositRequest, TransactionResponse
from app.services.transaction_service import deposit_money, withdraw_money
from app.services.transaction_service import get_transaction_history

router = APIRouter(
    prefix="/api/accounts",
    tags=["Accounts"]
)

@router.post(
    "/create",
    response_model=AccountResponse
)
def create_savings_account(
    account: AccountCreate,
    db: Session= Depends(get_db)
):
    return create_account(
        db=db,
        user_id=1,
        account_type=account.account_type
    )