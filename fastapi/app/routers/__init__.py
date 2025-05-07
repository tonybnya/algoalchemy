"""
Initialize and register all router modules for the FastAPI application.
"""

from fastapi import FastAPI


def register_routers(app: FastAPI) -> None:
    """
    Register all router modules with the FastAPI application.

    Args:
        app: The FastAPI application instance
    """
    # Import routers inside the function to avoid circular imports
    from app.routers.ping import router as ping_router
    from app.routers.root import router as root_router

    # from app.routers.user import router as user_router
    # from app.routers.blogpost import router as blogpost_router
    # Include routers with their prefixes
    app.include_router(ping_router, prefix="/api")
    app.include_router(root_router, prefix="/api")

    # app.include_router(user_router, prefix="/api/users")
    # app.include_router(blogpost_router, prefix="/api/blogposts")
