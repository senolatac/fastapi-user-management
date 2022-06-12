from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from app.config.database import Base, engine
from app.core.config import get_app_settings
from app.controller.routes import router as api_router


def get_application() -> FastAPI:
    settings = get_app_settings()

    Base.metadata.create_all(bind=engine)

    # '**' takes a dict and extracts its contents and passes them as parameters to a function.
    main_app = FastAPI(**settings.fastapi_kwargs)

    main_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    main_app.include_router(api_router)

    return main_app


app = get_application()
