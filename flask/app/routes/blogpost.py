"""
BlogPost routes/endpoints blueprint.
"""

from flask import Blueprint, jsonify

# Define a blueprint for blogpost routes/endpoints.
blogpost_bp = Blueprint("blogposts", __name__)


@blogpost_bp.route("/<user_id>", methods=["POST"])
def create_blogpost(user_id: int):
    """
    Endpoint to CREATE a new blogpost.
    """
    pass


@blogpost_bp.route("/", methods=["GET"])
def read_all_blogposts():
    """
    Endpoint to READ all the blogposts.
    """
    pass


@blogpost_bp.route("/<blogpost_id>", methods=["GET"])
def read_blogpost(blogpost_id: int):
    """
    Endpoint to READ a blogpost.
    """
    pass


@blogpost_bp.route("/<blogpost_id>", methods=["PUT"])
def update_blogpost(blogpost_id: int):
    """
    Endpoint to UPDATE a blogpost.
    """
    pass


@blogpost_bp.route("/<blogpost_id>", methods=["DELETE"])
def delete_blogpost(blogpost_id: int):
    """
    Endpoint to DELETE a blogpost.
    """
    pass
