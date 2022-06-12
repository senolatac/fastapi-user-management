from fastapi import APIRouter

from app.controller.endpoint import user_endpoints, admin_endpoints, authentication_endpoints

router = APIRouter()
router.include_router(authentication_endpoints.router)
router.include_router(user_endpoints.router)
router.include_router(admin_endpoints.router)
