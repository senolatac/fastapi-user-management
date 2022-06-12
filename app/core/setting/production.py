import logging
from app.core.setting.app import AppSettings


class ProdAppSettings(AppSettings):
    debug: bool = False
    logging_level: int = logging.INFO
