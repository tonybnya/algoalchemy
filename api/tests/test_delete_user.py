"""
Tests for delete user route/endpoint.
"""

from app import create_app


def test_delete_non_existing_user():
    """
    Test `/api/users/{id}` route
    returns 404 with meaningful message.
    """
    app = create_app()
    client = app.test_client()

    # make sure the id doesn't exist in the db
    response = client.delete("/api/users/55")

    assert response.status_code == 404
    assert isinstance(response.get_json(), dict)
    assert "message" in response.get_json()
    assert response.get_json() == {"message": "User not found"}


def test_delete_existing_user():
    """
    Test `/api/users/{id}` route
    returns 204 OK and correct body response with empty dict.
    """
    app = create_app()
    client = app.test_client()

    # make sure the id do exist in the db
    response = client.delete("/api/users/7")

    assert response.status_code == 204
