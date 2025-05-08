"""
Tests for READ users in ascending order route/endpoint.
"""

from app import create_app
from app.models.user import User


def test_descending_id():
    """
    Test `/api/users/ascending_id` route
    returns 200 OK and data in the correct order.
    """
    app = create_app()
    client = app.test_client()

    # # Generate unique username and email using timestamp and UUID
    # timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    # unique_id = str(uuid.uuid4())[:8]

    response = client.get("/api/users/ascending_id")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
    users: list[User] = response.get_json()
    assert users[0].get("id") == 1
    # Verify IDs are in ascending order
    for i in range(1, len(users)):
        assert users[i].get("id") > users[i-1].get("id"), "IDs should be in ascending order"
