from typing import Optional

from pydantic import BaseModel


class UserPrinciple(BaseModel):
    id: int
    username: str
    role: str
    token: Optional[str] = None
