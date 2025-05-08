"""
Tests for create user route/endpoint.
"""

from app import create_app

# Uncomment this test the first time you run pytest
# then comment it, since the user created will already be in the db
# def test_create_user():
#     """
#     Test `/api/users` route
#     returns 201 OK and correct body response for successfull creation.
#     """
#     app = create_app()
#     client = app.test_client()
#
#     response = client.post(
#         "/api/users",
#         json={
#             "username": f"Ma go",
#             "email": f"mago@exceltogether.cm",
#             "address": "Makepe Missoke, Douala - Cameroun",
#             "phone": "+237699995153",
#         },
#     )
#     assert response.status_code == 201
#     assert response.get_json() == {"message": "User created"}


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
            "username": "Ma go",
            "email": "mago@exceltogether.cm",
            "address": "Makepe Missoke, Douala - Cameroun",
            "phone": "+237699995153",
        },
    )
    assert response.status_code == 409
    assert response.get_json() == {
        "message": "User with that username or email already exists"
    }


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
