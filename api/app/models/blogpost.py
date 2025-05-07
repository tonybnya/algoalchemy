"""
Modelisation of a blogpost.
"""

from datetime import datetime

from sqlalchemy.orm import relationship

from app import db


class BlogPost(db.Model):
    """
    BlogPost class mapping the table "blogposts" in the database.
    """

    __tablename__ = "blogposts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(500))
    date = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # Define relationship to User
    user = relationship("User", back_populates="posts")

    def __repr__(self) -> str:
        """
        String representation of a blogpost.
        """
        return f"<BlogPost {self.title}>"
