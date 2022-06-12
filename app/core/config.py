from functools import lru_cache
from typing import Dict, Type

from app.core.setting.app import AppSettings
from app.core.setting.base import AppEnvTypes, BaseAppSettings
from app.core.setting.development import DevAppSettings
from app.core.setting.production import ProdAppSettings
from app.core.setting.test import TestAppSettings

environments: Dict[AppEnvTypes, Type[AppSettings]] = {
    AppEnvTypes.dev: DevAppSettings,
    AppEnvTypes.prod: ProdAppSettings,
    AppEnvTypes.test: TestAppSettings,
}


@lru_cache
def get_app_settings() -> AppSettings:
    app_env = BaseAppSettings().app_env
    config = environments[app_env]
    return config()
