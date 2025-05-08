"""
Tests for update user route/endpoint.
"""

from app import create_app


def test_update_non_existing_user():
    """
    Test `/api/users/{id}` route
    returns 404 with meaningful message.
    """
    app = create_app()
    client = app.test_client()

    # make sure the id doesn't exist in the db
    response = client.put(
        "/api/users/55",
        json={
            "username": "username",
            "email": "username@example.cm",
            "address": "Douala - Cameroun",
            "phone": "+237699995153",
        },
    )

    assert response.status_code == 404
    assert isinstance(response.get_json(), dict)
    assert "message" in response.get_json()
    assert response.get_json() == {"message": "User not found"}


def test_update_with_no_data_provided():
    """
    Test `/api/users{id}` route
    Returns 400 with meaningful message
    """
    app = create_app()
    client = app.test_client()

    # make sure the id doesn't exist in the db
    response = client.put("/api/users/2", json={})

    assert response.status_code == 400
    assert isinstance(response.get_json(), dict)
    assert "message" in response.get_json()
    assert response.get_json() == {"message": "No data provided"}


def test_update_existing_user():
    """
    Test `/api/users/{id}` route
    returns 200 OK and correct body response with updated data.
    """
    app = create_app()
    client = app.test_client()

    # make sure the id do exist in the db
    response = client.put(
        "/api/users/2",
        json={
            "username": "username",
            "email": "username@example.cm",
            "address": "Douala - Cameroun",
            "phone": "+237699995153",
        },
    )

    assert isinstance(response.get_json(), dict)

    assert response.get_json().get("username") == "username"
    assert response.get_json().get("email") == "username@example.cm"
    assert response.get_json().get("address") == "Douala - Cameroun"
    assert response.get_json().get("phone") == "+237699995153"

    assert response.status_code == 200
