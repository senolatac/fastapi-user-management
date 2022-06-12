from fastapi import HTTPException, status
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.schema.user import UserBase
from app.security import jwt_provider
from app.security.user_principle import UserPrinciple
from app.service import user_service

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(db: Session, sign_in_request: UserBase):
    user = user_service.find_by_username(db, sign_in_request.username)
    if not user:
        return False
    if not verify_password(sign_in_request.password, user.password):
        return False
    return UserPrinciple(id=user.id, username=user.username, role=user.role)


def sign_in_and_return_jwt(db: Session, sign_in_request: UserBase):
    user = authenticate_user(db, sign_in_request)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    jwt = jwt_provider.generate_token(user)
    user.token = jwt
    return user
