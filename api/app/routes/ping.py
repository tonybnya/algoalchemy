"""
Ping route/endpoint blueprint.
"""

from flask import Blueprint, jsonify

# Define a blueprint for ping route/endpoint
ping_bp = Blueprint("ping", __name__)


@ping_bp.route("/ping", methods=["GET"])
def ping():
    """
    Simple route/endpoint to test the server responsiveness.
    """
    return jsonify({"message": "pong"}), 200
