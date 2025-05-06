"""
Tests for ping route/endpoint.
"""

from app import create_app


def test_ping():
    """
    Test `/api/ping` route returns 200 OK and correct body response.
    """
    app = create_app()
    client = app.test_client()

    response = client.get("/api/ping")
    assert response.status_code == 200
    assert response.get_json() == {"message": "pong"}
