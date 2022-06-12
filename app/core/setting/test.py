import logging
from typing import Dict, Any

from app.core.setting.app import AppSettings


class TestAppSettings(AppSettings):
    debug: bool = True

    logging_level: int = logging.DEBUG

    database_url = "sqlite:///:memory:"

    class Config(AppSettings.Config):
        env_file = "test.env"

    @property
    def connect_ags(self) -> Dict[str, Any]:
        return {
            "check_same_thread": False
        }
