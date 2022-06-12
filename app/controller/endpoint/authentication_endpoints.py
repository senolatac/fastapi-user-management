from fastapi import APIRouter, Depends, Body, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import Required
from sqlalchemy.orm import Session

from app.dependency.database import get_db
from app.schema import user
from app.schema.user import UserBase
from app.service import user_service, authentication_service

router = APIRouter(
    prefix="/authentication",
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)


@router.post("/sign-up")
async def sign_up(user_body: user.UserCreate = Body(default=Required), db: Session = Depends(get_db)):
    if user_service.find_by_username(db, username=user_body.username) is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already exist")
    return user_service.create_user(db, user=user_body)


@router.post("/sign-in")
async def sign_in(user_body: UserBase = Body(default=Required), db: Session = Depends(get_db)):
    return authentication_service.sign_in_and_return_jwt(db, sign_in_request=user_body)


@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user_body = UserBase(username=form_data.username, password=form_data.password)
    auth_user = authentication_service.sign_in_and_return_jwt(db, sign_in_request=user_body)
    return {"access_token": auth_user.token, "token_type": "bearer"}

