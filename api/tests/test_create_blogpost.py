"""
Tests for create blogpost route/endpoint.
"""

from app import create_app


def test_create_blogpost():
    """
    Test `/api/blogposts/{user_id}` route
    returns 201 OK and correct body response for successfull creation.
    """
    app = create_app()
    client = app.test_client()

    # ensure the id do exist in the database
    response = client.post(
        "/api/blogposts/12", json={"title": "Ma go", "body": "This is a post."}
    )
    assert response.status_code == 201
    assert response.get_json() == {"message": "Blogpost created"}


def test_create_blogpost_with_missing_parameter():
    """
    Test `/api/blogposts/{user_id}` route
    returns 400 for missing parameters.
    """
    app = create_app()
    client = app.test_client()

    # ensure the id do exist in the database
    response = client.post(
        "/api/blogposts/12", json={"title": "", "body": "A new post."}
    )
    assert response.status_code == 400
    assert response.get_json() == {"message": "Missing required fields"}


def test_create_blogpost_with_non_existing_user():
    """
    Test `/api/blogposts/{user_id}` route
    returns 400 for non existing user.
    """
    app = create_app()
    client = app.test_client()

    # ensure the id does not exist in the database
    response = client.post(
        "/api/blogposts/55", json={"title": "New post", "body": "A new post body."}
    )
    assert response.status_code == 400
    assert response.get_json() == {"message": "User does not exist"}
