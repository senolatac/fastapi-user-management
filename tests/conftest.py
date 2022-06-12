import os
from typing import Any
from typing import Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from tests.utils.user import authentication_token_for_user, authentication_token_for_admin

os.environ["APP_ENV"] = "test"


def start_application():
    from app.main import get_application  # local import for testing purpose

    return get_application()


@pytest.fixture
def app() -> Generator[FastAPI, Any, None]:
    _app = start_application()
    yield _app


@pytest.fixture
def client(
        app: FastAPI
) -> Generator[TestClient, Any, None]:
    with TestClient(app) as client:
        yield client


@pytest.fixture
def authorized_client_user(client: TestClient) -> TestClient:
    jwt = authentication_token_for_user(client)
    client.headers = {
        "Authorization": f"Bearer {jwt}",
        **client.headers,
    }
    return client


@pytest.fixture
def authorized_client_admin(client: TestClient) -> TestClient:
    jwt = authentication_token_for_admin(client)
    client.headers["Authorization"] = f"Bearer {jwt}"
    return client
