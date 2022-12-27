""" Database models """
import json
from database import db


class User(db.Model):
    """User model"""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=True)

    def __repr__(self):
        return f"<User {self.email}>"

    def __str__(self):
        return f"<User {self.email}>"



db.create_all()