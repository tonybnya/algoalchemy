"""
Root route/endpoint blueprint.
"""

from flask import Blueprint, jsonify

# Define a blueprint for root route/endpoint
root_bp = Blueprint("root", __name__)


@root_bp.route("", methods=["GET"])
def root():
    """
    Simple route/endpoint to test the root.
    """
    return (
        jsonify(
            {
                "message": "A clever mix of algorithms and the magic (alchemy) of Python, implemented with both Flask and FastAPI."
            }
        ),
        200,
    )
