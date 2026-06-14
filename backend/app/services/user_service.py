from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserRegister
from app.core.security import hash_password
from app.core.security import verify_password
from app.core.security import create_access_token

def create_user(
        db: Session,
        user: UserRegister
):
    existing_user = (
        db.query(User).filter(
            User.email == user.email
        ).first()
    )

    if existing_user:
        return None
    
    db_user = User(
        full_name=user.full_name,
        email=user.email,
        password_hash=hash_password(
            user.password
        )
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def login_user(
        db: Session,
        email: str,
        password: str
):
    user = (
        db.query(User).filter(User.email==email)
        .first()
    )
    if not user:
        return None
    
    if not verify_password(
        password,
        user.password_hash
    ):
        return None
    
    token = create_access_token(
        {
            "sub": user.email
        }
    )

    return token