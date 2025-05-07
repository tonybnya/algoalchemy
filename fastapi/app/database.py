"""
Database configuration for the FastAPI application.
"""

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Load environment variables
load_dotenv()

# Get the project root directory (two levels up from this file)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

# Use environment variable or construct absolute path to SQLite DB at project root
DB_PATH = os.getenv("DATABASE_URI")
if not DB_PATH or DB_PATH.startswith("sqlite:///"):
    # Create absolute path to the database in the project root
    db_file = os.path.join(PROJECT_ROOT, "algoalchemy.db")
    DATABASE_URI = f"sqlite:///{db_file}"
else:
    DATABASE_URI = DB_PATH

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URI, connect_args={"check_same_thread": False}  # Only needed for SQLite
)

# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for models
Base = declarative_base()


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
