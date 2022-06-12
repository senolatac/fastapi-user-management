def test_get_all_users(authorized_client_admin):
    response = authorized_client_admin.get("/admin/all-users")

    assert response.status_code == 200
    assert response.json() is not None
    assert len(response.json()) == 1
