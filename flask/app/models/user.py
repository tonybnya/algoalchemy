"""
Modelisation of a user.
"""

from sqlalchemy.orm import relationship

from app import db


class User(db.Model):
    """
    User class mapping the table "users" in the database.
    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    posts = relationship("BlogPost", back_populates="user")

    def __repr__(self) -> str:
        """
        String representation of a user.
        """
        return f"<User {self.username}>"
