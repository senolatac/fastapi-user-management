import logging

from app.core.setting.app import AppSettings


class DevAppSettings(AppSettings):
    debug: bool = True

    logging_level: int = logging.DEBUG

    class Config(AppSettings.Config):
        env_file = "dev.env"
