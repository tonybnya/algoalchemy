"""
Tests for create user route/endpoint.
"""

import datetime
import uuid

from app import create_app


def test_create_user():
    """
    Test `/api/users` route
    returns 201 OK and correct body response for successfull creation.
    """
    app = create_app()
    client = app.test_client()

    # Generate unique username and email using timestamp and UUID
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    unique_id = str(uuid.uuid4())[:8]

    response = client.post(
        "/api/users",
        json={
            "username": f"Mfon_{timestamp}_{unique_id}",
            "email": f"test_{timestamp}_{unique_id}@example.com",
            "address": "Ndogbong, lieu-dit carrefour Bifaga, Douala - Cameroun",
            "phone": "+237694639475",
        },
    )
    assert response.status_code == 201
    assert response.get_json() == {"message": "User created"}


def test_missing_parameter():
    """
    Test `/api/users` route
    returns 400 for missing parameters.
    """
    app = create_app()
    client = app.test_client()

    response = client.post(
        "/api/users",
        json={
            "username": "",
            "email": "fakemail@example.com",
            "address": "fake address",
            "phone": "",
        },
    )
    assert response.status_code == 400
    assert response.get_json() == {"message": "Missing required fields"}


def test_existing_user():
    """
    Test `/api/users` route
    returns 409 for existing user.
    """
    app = create_app()
    client = app.test_client()

    response = client.post(
        "/api/users",
        json={
            "username": "Mfon",
            "email": "saoudayazieya@gmail.com",
            "address": "Ndogbong, lieu-dit carrefour Bifaga, Douala - Cameroun",
            "phone": "+237694639475",
        },
    )
    assert response.status_code == 409
    assert response.get_json() == {
        "message": "User with that username or email already exists"
    }


# def test_unexpected_error():
#     """
#     Test `/error` route
#     returns 500 for unexpected error.
#     """
#     app = create_app()
#     client = app.test_client()
#
#     assert response.status_code == 500
