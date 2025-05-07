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
                "message": "A clever mix of Data Structures and Algorithms (DSA) and the magic (alchemy) of Python, implemented with Flask."
            }
        ),
        200,
    )
