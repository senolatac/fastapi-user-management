import datetime

from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.model.role import Role
from app.model.user import User
from app.repository import user_repository
from app.schema.user import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(db: Session, user: UserCreate):
    password = pwd_context.hash(user.password)
    create_time = datetime.datetime.now()

    user = User(username=user.username, password=password, name=user.name, create_time=create_time,
                role=Role.USER.value)

    return user_repository.create_user(db, user)


def find_by_username(db: Session, username: str):
    return user_repository.get_user_by_username(db, username)


def find_all_users(db: Session):
    return user_repository.get_all_users(db)


def change_role(db: Session, username: str, new_role: Role):
    user_repository.update_user_role(db, username, new_role)
