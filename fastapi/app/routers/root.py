"""
Root router/endpoint module.
"""

from fastapi import APIRouter

# Create a router for root endpoint
router = APIRouter()


@router.get("", response_model=dict[str, str])
async def root():
    """
    Simple endpoint to describe the API.

    Returns:
        dict: A simple message with the description of the API.
    """
    return {
        "message": "A clever mix of algorithms and the magic (alchemy) of Python, implemented with both Flask and FastAPI."
    }
