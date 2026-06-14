from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.db import get_db

from app.schemas.transaction_schema import DepositRequest, WithdrawRequest, DepositResponse
from app.schemas.transaction_schema import TransactionResponse, TransferRequest, TransferResponse
from app.services.transaction_service import deposit_money, get_transaction_history, withdraw_money
from app.services.transaction_service import transfer_money

router = APIRouter(
    prefix="/api/transactions",
    tags=["Transactions"]
)

@router.post(
        "/deposit",
        response_model=DepositResponse
)
def deposit(
    request: DepositRequest,
    db: Session=Depends(get_db)
):
    return deposit_money(
        db=db,
        account_number=request.account_number,
        amount=request.amount,
        description=request.description
    )

@router.post(
        "/withdraw"
)
def withdraw(
    request: WithdrawRequest,
    db: Session=Depends(get_db)
):
    return withdraw_money(
        db=db,
        account_number=request.account_number,
        amount=request.amount
    )

@router.get(
        "/transactions/{account_number}",
        response_model=list[TransactionResponse]
)
def transaction_history(
        account_number: str,
        db: Session=Depends(get_db)
):
    return get_transaction_history(
        db,
        account_number
    )

@router.post(
        "/transfer",
        response_model=TransferResponse
)
def transfer(
        request: TransferRequest,
        db: Session=Depends(get_db)
):
    return transfer_money(
        db=db,
        from_account=request.from_account,
        to_account=request.to_account,
        amount=request.amount
    )