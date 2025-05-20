"""
Initialize the Flask application and register all the routes/endpoints.
"""

import sqlite3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import event
from sqlalchemy.engine import Engine

from app.config import Config

# Create an instance of a SQLAlchemy object
db = SQLAlchemy()


def create_app() -> Flask:
    """
    Application factory to create and configure the Flask application.
    """
    flask_app = Flask(__name__)
    flask_app.config.from_object(Config)

    # Enable CORS for all routes
    CORS(flask_app)

    # Configure SQLite3 to enforce foreign key constraints
    @event.listens_for(Engine, "connect")
    def set_sqlite_pragma(dbapi_connection, connection_record):
        if isinstance(dbapi_connection, sqlite3.Connection):
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON;")
            cursor.close()

    # Initialize the app
    db.init_app(flask_app)

    # Import all models to ensure they're loaded
    import app.models

    # Register all the routes/endpoints of the application (blueprints)
    from app.routes import register_routes
    register_routes(flask_app)

    return flask_app
