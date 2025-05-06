import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """
    Class configuration for Flask settings and database.
    """

    SECRET_KEY: str = os.getenv("SECRET_KEY", "default_secret")
    DEBUG: bool = os.getenv("DEBUG", True)
    SQLALCHEMY_DATABASE_URI: str = os.getenv("DATABASE_URI", "sqlite:///algoalchemy.db")
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
