"""
BlogPost routes/endpoints blueprint.
"""

import os
import sys
from datetime import datetime

from flask import Blueprint, jsonify, request

from app import db
from app.models.blogpost import BlogPost
from app.models.user import User
from dsa.hashmap import HashMap

# Add the parent directory of the app directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(parent_dir)


# Define a blueprint for blogpost routes/endpoints.
blogpost_bp = Blueprint("blogposts", __name__)


@blogpost_bp.route("/<user_id>", methods=["POST"])
def create_blogpost(user_id: int):
    """
    Endpoint to CREATE a new blogpost.
    """
    user = User.query.filter_by(id=user_id).first()

    if not user:
        return jsonify({"message": "User does not exist"}), 400

    data = request.get_json()

    # Validate required fields
    required_fields = ["title", "body"]
    if not all(field in data and data.get(field) for field in required_fields):
        return jsonify({"message": "Missing required fields"}), 400

    # try:
    hashmap = HashMap(10)
    hashmap.add_key_value("title", data["title"])
    hashmap.add_key_value("body", data["body"])
    hashmap.add_key_value("date", datetime.now())
    hashmap.add_key_value("user_id", user_id)

    try:
        new_blogpost = BlogPost(
            title=hashmap.get_value("title"),
            body=hashmap.get_value("body"),
            date=hashmap.get_value("date"),
            user_id=hashmap.get_value("user_id"),
        )
        db.session.add(new_blogpost)
        db.session.commit()
        return jsonify({"message": "Blogpost created"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500


# @blogpost_bp.route("/", methods=["GET"])
# def read_all_blogposts():
#     """
#     Endpoint to READ all the blogposts.
#     """
#     pass
#
#
# @blogpost_bp.route("/<blogpost_id>", methods=["GET"])
# def read_blogpost(blogpost_id: int):
#     """
#     Endpoint to READ a blogpost.
#     """
#     pass
#
#
# @blogpost_bp.route("/<blogpost_id>", methods=["PUT"])
# def update_blogpost(blogpost_id: int):
#     """
#     Endpoint to UPDATE a blogpost.
#     """
#     pass
#
#
# @blogpost_bp.route("/<blogpost_id>", methods=["DELETE"])
# def delete_blogpost(blogpost_id: int):
#     """
#     Endpoint to DELETE a blogpost.
#     """
#     pass
