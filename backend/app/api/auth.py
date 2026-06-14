from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.db import get_db

from app.schemas.user_schema import UserRegister, UserResponse, TokenResponse, UserLogin
from app.services.user_service import create_user, login_user


router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)

@router.get("/health")
def health():
    return {
        "message": "Auth Module Ready"
    }

@router.post("/register", response_model=UserResponse)
def register_user(
    user: UserRegister,
    db: Session = Depends(get_db)
):
    db_user = create_user(
        db,
        user
    )
    if db_user is None:
        return {
            "message": "User already Exists"
        }
    return db_user

@router.post(
        "/login", response_model=TokenResponse
)
def login(
    user: UserLogin,
    db: Session=Depends(get_db)
):
    
    token = login_user(
        db,
        user.email,
        user.password
    )

    if token is None:
        return {
            "access_token": "",
            "token_type": "bearer"
        }
    
    return {
        "access_token": token,
        "token_type": "bearer"
    }