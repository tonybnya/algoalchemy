"""
Pytest configuration file for FastAPI tests
"""
import sys
import os
import pytest
from fastapi.testclient import TestClient

# Add the fastapi directory to Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

# Import the FastAPI app
from main import app

@pytest.fixture
def client():
    """
    Fixture that provides a FastAPI TestClient for testing endpoints
    """
    return TestClient(app)

