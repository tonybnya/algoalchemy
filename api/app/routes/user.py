"""
User routes/endpoints blueprint.
"""

import os
import sys

from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

# Add the parent directory of the app directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(parent_dir)

from app import db
from app.models.user import User
from dsa.linked_list import LinkedList

# Define a blueprint for user routes/endpoints.
user_bp = Blueprint("users", __name__)


@user_bp.route("", methods=["POST"])
def create_user():
    """
    Endpoint to CREATE a new user.
    """
    data = request.get_json()

    # Validate required fields
    required_fields = ["username", "email", "address", "phone"]
    if not all(field in data and data.get(field) for field in required_fields):
        return jsonify({"message": "Missing required fields"}), 400

    # Check for duplicate username or email
    existing_user = User.query.filter(
        (User.username == data.get("username") or User.email == data.get("email"))
    ).first()

    if existing_user:
        return (
            jsonify({"message": "User with that username or email already exists"}),
            409,
        )

    try:
        new_user = User(
            username=data.get("username"),
            email=data.get("email"),
            address=data.get("address"),
            phone=data.get("phone"),
        )

        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User created"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500


@user_bp.route("/descending_id", methods=["GET"])
def get_users_in_descending_order():
    """
    Endpoint to READ all users by IDs in descending order
    """
    users: list[User] = User.query.all()
    users_ll = LinkedList()

    for user in users:
        users_ll.add_to_head(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "address": user.address,
                "phone": user.phone,
            }
        )

    return jsonify(users_ll.ll_to_list()), 200


@user_bp.route("/ascending_id", methods=["GET"])
def get_users_in_ascending_order():
    """
    Endpoint to READ all users by IDs in ascending order
    Inserting at the linked list here is redundant, since
    by default, `User.query.all()` arrange the data in ascending order
    """
    users: list[User] = User.query.all()
    users_ll = LinkedList()

    for user in users:
        users_ll.add_to_tail(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "address": user.address,
                "phone": user.phone,
            }
        )

    return jsonify(users_ll.ll_to_list()), 200


@user_bp.route("/<user_id>", methods=["GET"])
def read_user(user_id: int):
    """
    Endpoint to READ a user.
    """
    users: list[User] = User.query.all()
    users_ll = LinkedList()

    for user in users:
        users_ll.add_to_head(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "address": user.address,
                "phone": user.phone,
            }
        )

    user: User = users_ll.get_user_by_id(user_id)

    return jsonify(user), 200


@user_bp.route("/<user_id>/blogposts", methods=["GET"])
def read_all_blogposts(user_id: int):
    """
    Endpoint to READ all the blogposts of a user.
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
