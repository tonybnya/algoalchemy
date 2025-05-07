"""
Tests for root route/endpoint.
"""

from app import create_app


def test_root():
    """
    Test `/api` route returns 200 OK and correct body response.
    """
    app = create_app()
    client = app.test_client()

    response = client.get("/api")
    assert response.status_code == 200
    assert response.get_json() == {
        "message": "A clever mix of algorithms and the magic (alchemy) of Python, implemented with both Flask and FastAPI."
    }
