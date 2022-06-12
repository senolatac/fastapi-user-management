import logging
from typing import List

from fastapi import Depends, HTTPException, status

from app.security.jwt_provider import get_authentication
from app.security.user_principle import UserPrinciple


class RoleChecker:
    
    """constructor => roleChecker = RoleChecker([])"""
    def __init__(self, allowed_roles: List):
        """

        :type allowed_roles: List of roles
        """
        self.allowed_roles = allowed_roles

    # call created object => roleChecker()
    def __call__(self, user: UserPrinciple = Depends(get_authentication)):
        if user.role not in self.allowed_roles:
            logging.debug(f"User with role {user.role} not in {self.allowed_roles}")
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Operation not permitted")
