import logging
from typing import Any, Dict

from app.core.setting.base import BaseAppSettings


class AppSettings(BaseAppSettings):
    debug: bool = False
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "Fastapi Demo"
    version: str = "0.0.0"

    admin_key_token: str = "admin"
    secure_key: str = "user1,user2"

    logging_level: int = logging.INFO
    logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s', level=logging_level)

    database_url: str = "mysql://admin:1234@localhost:3306/db_user"

    jwt_secret_key: str = "random-string-key-secure-key"

    class Config:
        validate_assignment = True

    @property
    def connect_ags(self) -> Dict[str, Any]:
        return {}

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }
