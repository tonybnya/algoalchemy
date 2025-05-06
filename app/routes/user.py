"""
User routes/endpoints blueprint.
"""

from flask import Blueprint, jsonify, request

from app import db
from app.models.user import User

# Define a blueprint for user routes/endpoints.
user_bp = Blueprint("users", __name__)


@user_bp.route("/", methods=["POST"])
def create_user():
    """
    Endpoint to CREATE a new user.
    """
    data = request.get_json()

    new_user = User(
        username=data.get("username"),
        email=data.get("email"),
        address=data.get("address"),
        phone=data.get("phone"),
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created"}), 201


@user_bp.route("/ascending_ids", methods=["GET"])
def get_all_users_ascending():
    """
    Endpoint to READ all users by IDs in ascending order
    """
    pass


@user_bp.route("/descending_ids", methods=["GET"])
def get_all_users_descending():
    """
    Endpoint to READ all users by IDs in descending order
    """
    pass


@user_bp.route("/<user_id>/blogposts", methods=["GET"])
def read_all_blogposts(user_id: int):
    """
    Endpoint to READ all the blogposts of a user.
    """
    pass


@user_bp.route("/<user_id>", methods=["GET"])
def read_user(user_id: int):
    """
    Endpoint to READ a user.
    """
    pass


@user_bp.route("/<user_id>", methods=["PUT"])
def update_user(user_id: int):
    """
    Endpoint to UPDATE a user.
    """
    pass


@user_bp.route("/<user_id>", methods=["DELETE"])
def delete_user(user_id: int):
    """
    Endpoint to DELETE a user.
    """
    pass
