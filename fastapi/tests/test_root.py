"""
Tests for root endpoint in FastAPI implementation.
"""


def test_ping(client):
    """
    Test `/api` endpoint returns 200 OK and correct body response.

    Args:
        client: FastAPI TestClient fixture from conftest.py
    """
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == {
        "message": "A clever mix of algorithms and the magic (alchemy) of Python, implemented with both Flask and FastAPI."
    }
