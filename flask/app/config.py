import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the project root directory (two levels up from this file)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))


class Config:
    """
    Class configuration for Flask settings and database.
    """

    SECRET_KEY: str = os.getenv("SECRET_KEY", "default_secret")
    DEBUG: bool = os.getenv("DEBUG", True)
    
    # Use environment variable or construct absolute path to SQLite DB at project root
    DB_PATH = os.getenv("DATABASE_URI")
    if not DB_PATH or DB_PATH.startswith("sqlite:///"):
        # Create absolute path to the database in the project root
        db_file = os.path.join(PROJECT_ROOT, "algoalchemy.db")
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_file}"
    else:
        SQLALCHEMY_DATABASE_URI = DB_PATH
        
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
