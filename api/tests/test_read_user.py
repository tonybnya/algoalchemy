"""
Tests for read user route/endpoint.
"""

from app import create_app


def test_read_user():
    """
    Test `/api/users/{id}` route
    returns 200 OK and correct body response with a user info.
    """
    app = create_app()
    client = app.test_client()

    response = client.get("/api/users/1")

    assert response.status_code == 200
    assert "id" in response.get_json()
    assert "username" in response.get_json()
    assert "email" in response.get_json()
    assert "address" in response.get_json()
    assert "phone" in response.get_json()
    assert response.get_json() == {
        "id": 1,
        "username": "Kathleen Morton",
        "email": "Kathleen_Morton@email.com",
        "address": "59848 Frazier Inlet\nWest Gary, NY 01851",
        "phone": "5500917929027",
    }
    assert isinstance(response.get_json(), dict)
