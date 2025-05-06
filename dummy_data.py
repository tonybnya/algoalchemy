<<<<<<< HEAD
#!/usr/bin/env python3
"""
Generate dummy data for the AlgoAlchemy database.

This script can populate the database for either Flask, FastAPI, or both implementations.
"""

import argparse
import importlib.util
import os
import sys
from datetime import datetime
from random import randrange

from dotenv import load_dotenv
from faker import Faker

# Load environment variables
load_dotenv()

# Get project root directory
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Get database URI from environment or use absolute path to shared SQLite file
DB_PATH = os.getenv("DATABASE_URI")
if not DB_PATH or DB_PATH.startswith("sqlite:///"):
    # Create absolute path to the database in the project root
    db_file = os.path.join(PROJECT_ROOT, "algoalchemy.db")
    DATABASE_URI = f"sqlite:///{db_file}"
else:
    DATABASE_URI = DB_PATH

# Initialize faker
faker = Faker()


def populate_flask_db():
    """
    Populate the database using the Flask application context.
    """
    print("Populating database for Flask implementation...")

    # Add flask directory to the Python path
    flask_path = os.path.join(os.path.dirname(__file__), "flask")
    if flask_path not in sys.path:
        sys.path.insert(0, flask_path)

    try:
        # Import Flask app and models
        from flask.app import create_app, db
        from flask.app.models.blogpost import BlogPost
        from flask.app.models.user import User

        # Create the Flask app
        app = create_app()

        # Create an application context for database operations
        with app.app_context():
            # Create all tables in the database
            db.create_all()

            # Create dummy users
            for _ in range(200):
                username = faker.name()
                address = faker.address()
                phone = faker.msisdn()
                email = f'{username.replace(" ", "_")}@email.com'
                new_user = User(
                    username=username, address=address, phone=phone, email=email
                )
                db.session.add(new_user)
                db.session.commit()

            # Create dummy blog posts
            for _ in range(200):
                title = faker.sentence(5)
                body = faker.paragraph(190)
                date = faker.date_time()
                user_id = randrange(1, 200)

                new_blogpost = BlogPost(
                    title=title, body=body, date=date, user_id=user_id
                )
                db.session.add(new_blogpost)
                db.session.commit()

        print("Successfully populated database for Flask implementation!")
    except ImportError as e:
        print(f"Error importing Flask modules: {e}")
        return False
    except Exception as e:
        print(f"Error populating Flask database: {e}")
        return False

    return True


def populate_fastapi_db():
    """
    Populate the database using the FastAPI SQLAlchemy session.
    """
    print("Populating database for FastAPI implementation...")

    # Add fastapi directory to the Python path
    fastapi_path = os.path.join(os.path.dirname(__file__), "fastapi")
    if fastapi_path not in sys.path:
        sys.path.insert(0, fastapi_path)

    try:
        # Since FastAPI models and database are not yet implemented
        # We'll provide the structure but comment it out until it's implemented
        print("FastAPI models not yet implemented. Skipping database population.")

        # Uncomment and adapt this code once FastAPI models are implemented
        """
        from fastapi.app.database import Base, engine, SessionLocal
        
        # Import FastAPI models (once they exist)
        # These would need to be created first in the FastAPI implementation
        from fastapi.app.models.user import User
        from fastapi.app.models.blogpost import BlogPost
        
        # Create all tables in the database
        Base.metadata.create_all(bind=engine)
        
        # Create a database session
        db = SessionLocal()
        
        try:
            # Create dummy users
            for _ in range(200):
                username = faker.name()
                address = faker.address()
                phone = faker.msisdn()
                email = f'{username.replace(" ", "_")}@email.com'
                new_user = User(username=username, address=address, phone=phone, email=email)
                db.add(new_user)
                db.commit()
                db.refresh(new_user)
            
            # Create dummy blog posts
            for _ in range(200):
                title = faker.sentence(5)
                body = faker.paragraph(190)
                date = faker.date_time()
                user_id = randrange(1, 200)
                
                new_blogpost = BlogPost(title=title, body=body, date=date, user_id=user_id)
                db.add(new_blogpost)
                db.commit()
                db.refresh(new_blogpost)
                
        finally:
            db.close()
        """

        print("Note: You'll need to implement the FastAPI models before this can work.")
        return False
    except ImportError as e:
        print(f"Error importing FastAPI modules: {e}")
        return False
    except Exception as e:
        print(f"Error populating FastAPI database: {e}")
        return False

    return True


def main():
    """
    Parse command-line arguments and populate the specified database(s).
    """
    parser = argparse.ArgumentParser(
        description="Generate dummy data for AlgoAlchemy database."
    )
    parser.add_argument(
        "implementation",
        choices=["flask", "fastapi", "both"],
        help="Which implementation to populate the database for",
    )

    args = parser.parse_args()

    success = True

    if args.implementation in ["flask", "both"]:
        if not populate_flask_db():
            success = False

    if args.implementation in ["fastapi", "both"]:
        if not populate_fastapi_db():
            success = False

    if success:
        print("Database population completed successfully.")
    else:
        print("Database population completed with errors.")
        sys.exit(1)


if __name__ == "__main__":
    main()
=======
from datetime import datetime
from random import randrange

from faker import Faker

from app import create_app, db
from app.models import blogpost, user

# Create the Flask app
app = create_app()
now = datetime.now()

faker = Faker()

# Create an application context for database operations
with app.app_context():
    # Create all tables in the database
    db.create_all()

    # create dummy users
    for _ in range(200):
        username = faker.name()
        address = faker.address()
        phone = faker.msisdn()
        email = f'{username.replace(" ", "_")}@email.com'
        new_user = user.User(username=username, address=address, phone=phone, email=email)
        db.session.add(new_user)
        db.session.commit()

    # create dummy blog posts
    for _ in range(200):
        title = faker.sentence(5)
        body = faker.paragraph(190)
        date = faker.date_time()
        user_id = randrange(1, 200)

        new_blogpost = blogpost.BlogPost(title=title, body=body, date=date, user_id=user_id)
        db.session.add(new_blogpost)
        db.session.commit()
>>>>>>> 93c9e23b62e93ec24f015c8a53a720cb41bb7a6d
