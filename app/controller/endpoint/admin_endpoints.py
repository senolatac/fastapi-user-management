from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependency.database import get_db
from app.model.role import Role
from app.security.role_checker import RoleChecker
from app.service import user_service

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
    responses={404: {"description": "Not found"}},
)

allow_create_resource = RoleChecker([Role.ADMIN.value])


@router.get("/all-users", dependencies=[Depends(allow_create_resource)])
async def get_all_users(db: Session = Depends(get_db)):
    return user_service.find_all_users(db=db)
