from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import get_app_settings
from sqlalchemy.pool import StaticPool

SETTINGS = get_app_settings()
engine = create_engine(SETTINGS.database_url, connect_args={**SETTINGS.connect_ags}, poolclass=StaticPool)

meta = MetaData()
conn = engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
