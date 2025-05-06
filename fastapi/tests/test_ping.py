"""
Tests for ping endpoint in FastAPI implementation.
"""

def test_ping(client):
    """
    Test `/api/ping` endpoint returns 200 OK and correct body response.
    
    Args:
        client: FastAPI TestClient fixture from conftest.py
    """
    response = client.get("/api/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}

