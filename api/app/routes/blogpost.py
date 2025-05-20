"""
BlogPost routes/endpoints blueprint.
"""

import os
import random
import sys
from datetime import datetime

from flask import Blueprint, jsonify, request

from app import db
from app.models import blogpost
from app.models.blogpost import BlogPost
from app.models.user import User
from dsa import binary_search_tree, queue, stack
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


@blogpost_bp.route("/<blogpost_id>", methods=["GET"])
def read_blogpost(blogpost_id: int):
    """
    Endpoint to READ a blogpost.
    """
    blogposts = BlogPost.query.all()
    # blogposts are in ascending order by default
    # if we insert like that in the BST, we will end up with a linked list
    # so search for a specific blogpost will be in O(n) TC
    # we need to shuffle the blogposts so that the insert will end up
    # with something similar to a balanced BST
    random.shuffle(blogposts)

    bst = binary_search_tree.BST()

    for post in blogposts:
        bst.insert(
            {
                "id": post.id,
                "title": post.title,
                "body": post.body,
                "user_id": post.user_id,
            }
        )

    post = bst.search(blogpost_id)

    if not post:
        return jsonify({"message": "post not found"}), 404

    return jsonify(post), 200


@blogpost_bp.route("/numerics", methods=["GET"])
def get_numeric_post_bodies():
    """
    Endpoint to get blogposts, and process each body field,
    sum the ASCII values of each character in the body.
    """
    blogposts = BlogPost.query.all()
    q = queue.Queue()

    for post in blogposts:
        q.enqueue(post)

    response_list = []

    for _ in range(len(blogposts)):
        post = q.dequeue()
        numeric_body: int = 0
        for char in post.data.body:
            numeric_body += ord(char)

        post.data.body = numeric_body

        response_list.append(
            {
                "id": post.data.id,
                "title": post.data.title,
                "body": post.data.body,
                "user_id": post.data.user_id,
            }
        )

    return jsonify(response_list), 200


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


@blogpost_bp.route("/delete_last_10", methods=["DELETE"])
def delete_last_10_blogposts():
    """
    Endpoint to DELETE the last 10 blogposts.
    """
    blogposts = BlogPost.query.all()

    s = stack.Stack()

    for post in blogposts:
        s.push(post)

    for _ in range(10):
        deleted_post = s.pop()
        db.session.delete(deleted_post.data)
        db.session.commit()

    return jsonify({"message": "success"}), 204
