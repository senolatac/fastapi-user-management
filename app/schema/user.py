from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    password: str


class UserCreate(UserBase):
    name: str


class UserToken(UserCreate):
    token: str
