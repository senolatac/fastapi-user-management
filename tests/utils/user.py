import json
import random

from fastapi.testclient import TestClient


def user_authentication_headers(client: TestClient, username: str, password: str):
    data = {"username": username, "password": password}
    r = client.post("/authentication/sign-in", json.dumps(data))
    response = r.json()
    return response["token"]


def create_user(client: TestClient, username: str, password: str):
    data = {"username": username, "password": password, "name": username}
    client.post("/authentication/sign-up", json.dumps(data))


def update_user_role_as_admin(client: TestClient):
    client.put("/user/change/ADMIN")


def authentication_token_for_user(client: TestClient):
    username = "testU" + str(random.randint(0, 1000))
    password = "testU" + str(random.randint(0, 1000))

    create_user(client, username, password)

    return user_authentication_headers(client, username, password)


def authentication_token_for_admin(client: TestClient):
    username = "testA" + str(random.randint(0, 1000))
    password = "testA" + str(random.randint(0, 1000))

    create_user(client, username, password)

    token = user_authentication_headers(client, username, password)

    client.headers = {
        "Authorization": f"Bearer {token}",
        **client.headers,
    }

    update_user_role_as_admin(client)

    return user_authentication_headers(client, username, password)


