from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.account import Account
from app.models.transaction import Transaction

def deposit_money(
        db: Session,
        account_number: str,
        amount: float,
        description: str = None
):
    if amount <= 0:
        raise HTTPException(
            status_code=400,
            detail="Amount must be greater than zero"
        )
    account = (db.query(Account)
               .filter(
                   Account.account_number == account_number
                ).first()
    )
    if not account:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )
    if account.status != "ACTIVE":
        raise HTTPException(
            status_code=400,
            detail="Account is inactive"
        )
    
    account.balance += amount

    transaction = Transaction(
        account_id= account.id,
        transaction_type="DEPOSIT",
        amount=amount,
        balance_after_transaction=account.balance,
        description=description
    )
    db.add(transaction)
    db.commit()
    db.refresh(account)

    return {
        "message": "Ammount Deposited Successfully",
        "account_number": account.account_number,
        "balance": account.balance
    }

def withdraw_money(
    db,
    account_number,
    amount
):
    account = (
        db.query(Account)
        .filter(
            Account.account_number == account_number
        )
        .first()
    )

    if amount <= 0:
        raise HTTPException(
            status_code=400,
            detail="Amount must be greater than zero"
        )
    
    if account.status != "ACTIVE":
        raise HTTPException(
        status_code=400,
        detail="Account is inactive"
    )


    if not account:
        raise HTTPException(
            status_code=404,
            detail="Account Not Found"
        )

    if account.balance < amount:
        raise HTTPException(
            status_code=400,
            detail="Insufficient Funds"
        )

    account.balance -= amount

    transaction = Transaction(
        account_id=account.id,
        transaction_type="WITHDRAW",
        amount=amount,
        balance_after_transaction=account.balance,
        description="Cash Withdrawal"
    )

    db.add(transaction)
    db.commit()
    db.refresh(account)

    return {
        "message": "Withdrawal Successful",
        "account_number": account.account_number,
        "withdraw_amount": amount,
        "current_balance": account.balance
    }

def get_transaction_history(
        db,
        account_number
):
    account = (
        db.query(Account).filter(
            Account.account_number==account_number
        ).first()
    )

    if not account:
        raise Exception("Account not Found")
    
    transactions = (
        db.query(Transaction).filter(
            Transaction.account_id == account.id
        ).order_by(
            Transaction.created_at.desc()
        ).all()
    )

    return transactions


def transfer_money(
        db: Session,
        from_account: str,
        to_account: str,
        amount: float
):
    if amount <= 0:
        raise HTTPException(
            status_code=400,
            detail="Amount must be greater than zero"
        )
    
    source_account = (
        db.query(Account).filter(
            Account.account_number==from_account
        ).first()
    )

    destination_account = (
        db.query(Account).filter(
            Account.account_number==to_account
        ).first()
    )

    if not source_account:
        raise HTTPException(
            status_code=404,
            detail="Source account not found"
        )

    if not destination_account:
        raise HTTPException(
            status_code=404,
            detail="Destination account not found"
        )
    
    if source_account.account_number == destination_account.account_number:
        raise HTTPException(
            status_code=400,
            detail="Cannot transfer to same account"
        )
    
    if source_account.balance < amount:
        raise HTTPException(
            status_code=400,
            detail="Insufficient funds"
        )
    
    try:
        source_account.balance -= amount
        destination_account.balance += amount

        debit_transaction = Transaction(
            account_id=source_account.id,
            transaction_type="TRANSFER_DEBIT",
            amount=amount,
            balance_after_transaction=source_account.balance,
            description=f"Transfer to {to_account}"
        )

        credit_transaction = Transaction(
            account_id=destination_account.id,
            transaction_type="TRANSFER_CREDIT",
            amount=amount,
            balance_after_transaction=destination_account.balance,
            description=f"Transfer to {to_account}"
        )

        db.add(debit_transaction)
        db.add(credit_transaction)
        db.commit()
        return {
            "message": "Transfer Successful",
            "from_account": from_account,
            "to_account": to_account,
            "amount": amount
        }
    
    except Exception:
        db.rollback()
        raise