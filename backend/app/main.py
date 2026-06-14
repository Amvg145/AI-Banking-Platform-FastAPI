from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.account import router as account_router
from app.api.transaction import router as transaction_router

app = FastAPI(
    title="AI Banking System"
)

app.include_router(
    auth_router
)
app.include_router(
    account_router
)

app.include_router(
    transaction_router
)

@app.get("/")
def home():
    return {
        "message":
        "AI Banking Backend Running"
    }