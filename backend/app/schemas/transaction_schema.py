from pydantic import BaseModel
from datetime import datetime

class DepositRequest(BaseModel):
    account_number: str
    amount: float
    description: str = "Deposit"


class WithdrawRequest(BaseModel):
    account_number: str
    amount: float
    description: str = "Withdrawal"


class DepositResponse(BaseModel):
    message: str
    account_number: str
    balance: float


class TransactionResponse(BaseModel):
    transaction_type: str
    amount: float
    balance_after_transaction: float
    description: str
    created_at: datetime

    class Config:
        from_attributes = True


class TransferRequest(BaseModel):
    from_account: str
    to_account: str
    amount: float

class TransferResponse(BaseModel):
    message: str
    from_account: str
    to_account: str
    amount: float