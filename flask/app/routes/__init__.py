"""
Initialize and register all route/endpoint blueprints.
"""

from flask import Flask


def register_routes(flask_app: Flask) -> None:
    """
    Register all the blueprint routes/endpoints with the app.
    
    Args:
        flask_app: The Flask application instance
    """
    # Import blueprints inside the function to avoid circular imports
    from app.routes.blogpost import blogpost_bp
    from app.routes.ping import ping_bp
    from app.routes.user import user_bp
    
    # Register blueprints
    flask_app.register_blueprint(blogpost_bp, url_prefix="/api/blogposts")
    flask_app.register_blueprint(ping_bp, url_prefix="/api")
    flask_app.register_blueprint(user_bp, url_prefix="/api/users")
