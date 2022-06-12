import json


def test_sign_up(client):
    data = {
        "username": "test",
        "name": "test",
        "password": "test",
    }

    response = client.post("/authentication/sign-up", json.dumps(data))

    assert response.status_code == 200
    assert response.json()["id"] is not None
    assert response.json()["username"] == "test"
    assert response.json()["role"] == "USER"


def test_sign_in(client):
    data = {
        "username": "test",
        "password": "test",
    }

    response = client.post("/authentication/sign-in", json.dumps(data))

    assert response.status_code == 200
    assert response.json()["token"] is not None
    assert response.json()["username"] == "test"


def test_sign_in_wrong_username(client):
    data = {
        "username": "test1",
        "password": "test",
    }

    response = client.post("/authentication/sign-in", json.dumps(data))

    assert response.status_code == 401


def test_sign_in_wrong_password(client):
    data = {
        "username": "test",
        "password": "test1",
    }

    response = client.post("/authentication/sign-in", json.dumps(data))

    assert response.status_code == 401


def test_login_for_access_token(client):
    data = {
        "username": "test",
        "password": "test",
        "grant_type": "password",
    }

    response = client.post("/authentication/token", data, headers={"content-type": "application/x-www-form-urlencoded"})

    assert response.status_code == 200
    assert response.json()["access_token"] is not None
    assert response.json()["token_type"] == "bearer"
