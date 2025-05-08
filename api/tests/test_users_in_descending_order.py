"""
Tests for READ users in descending order route/endpoint.
"""

import datetime
import uuid

from app import create_app


def test_descending_id():
    """
    Test `/api/users/descending_id` route
    returns 200 OK and data in the correct order.
    """
    app = create_app()
    client = app.test_client()

    # # Generate unique username and email using timestamp and UUID
    # timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    # unique_id = str(uuid.uuid4())[:8]

    response = client.get("/api/users/descending_id")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
    users: list[User] = response.get_json()
    assert users[-1].get("id") == 1
    assert users[0].get("id") == len(users)
