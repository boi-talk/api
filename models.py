""" Database models """
from database import db
from datetime import datetime


class User(db.Model):
    """User model"""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f"<User {self.email}>"

    def __str__(self):
        return f"<User {self.email}>"


class Post(db.Model):
    """Post model"""

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("users", lazy=True))
    body = db.Column(db.String(256), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<Post {self.body}>"

    def __str__(self):
        return f"<Post {self.body}>"
