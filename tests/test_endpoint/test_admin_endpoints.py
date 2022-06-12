def test_get_all_users(authorized_client_admin):
    response = authorized_client_admin.get("/admin/all-users")

    assert response.status_code == 200
    assert response.json() is not None
    assert len(response.json()) == 1


def test_get_all_users_forbidden(authorized_client_user):
    response = authorized_client_user.get("/admin/all-users")

    assert response.status_code == 403


def test_get_all_users_jwt_error(client):
    client.headers["Authorization"] = "Bearer random"
    response = client.get("/admin/all-users")

    assert response.status_code == 401
