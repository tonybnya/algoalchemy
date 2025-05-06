"""
Ping router/endpoint module.
"""

from fastapi import APIRouter

# Create a router for ping endpoint
router = APIRouter()

@router.get("/ping")
async def ping():
    """
    Simple endpoint to test the server responsiveness.
    
    Returns:
        dict: A simple message indicating the server is alive
    """
    return {"message": "pong"}

