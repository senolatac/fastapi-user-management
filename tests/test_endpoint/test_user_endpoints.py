def test_get_current_user(authorized_client_user):
    response = authorized_client_user.get("/user/current-user")

    assert response.status_code == 200
    assert response.json()["id"] is not None
    assert response.json()["role"] == "USER"


def test_change_role(authorized_client_user):
    response = authorized_client_user.put("/user/change/ADMIN")

    assert response.status_code == 200
    assert response.json() is not None
    assert response.json() == True
