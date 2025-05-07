"""
Generate dummy data for the AlgoAlchemy database.
This script populates the database for Flask.
"""

import os
import sys
from datetime import datetime
from random import randrange

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import blogpost, user
from faker import Faker

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
        new_user = user.User(
            username=username, address=address, phone=phone, email=email
        )
        db.session.add(new_user)
        db.session.commit()

    # create dummy blog posts
    for _ in range(200):
        title = faker.sentence(5)
        body = faker.paragraph(190)
        date = faker.date_time()
        user_id = randrange(1, 200)

        new_blogpost = blogpost.BlogPost(
            title=title, body=body, date=date, user_id=user_id
        )
        db.session.add(new_blogpost)
        db.session.commit()
