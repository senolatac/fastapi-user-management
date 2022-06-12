from fastapi import APIRouter, Depends, Path
from pydantic import Required
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.model.role import Role
from app.security.jwt_provider import get_authentication
from app.security.user_principle import UserPrinciple
from app.service import user_service

router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)


@router.get("/current-user")
async def get_current_user(current_user: UserPrinciple = Depends(get_authentication)):
    return current_user


@router.put("/change/{role}")
async def change_role(role: Role = Path(default=Required), current_user: UserPrinciple = Depends(get_authentication),
                      db: Session = Depends(get_db)):
    user_service.change_role(db=db, username=current_user.username, new_role=role)
    return True
