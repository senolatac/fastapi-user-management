from sqlalchemy.orm import Session

from ..model.role import Role
from ..model.user import User


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_user_role(db: Session, username: str, role: Role):
    db.query(User).filter(User.username == username).update({'role': role.value})
    db.commit()
