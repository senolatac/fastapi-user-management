from sqlalchemy import Column, Integer, String, DateTime
from app.config.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    create_time = Column(DateTime, nullable=False)
    role = Column(String(16), nullable=False)
