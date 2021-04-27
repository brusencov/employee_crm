from datetime import datetime

from config import db


class UserRole:
    ADMIN = 1
    EMPLOYEE = 0


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(130), unique=True, nullable=False)
    phone = db.Column(db.String(90), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    role = db.Column(db.Integer, default=UserRole.EMPLOYEE)
    position = db.Column(db.String(100), nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)

    def __repr__(self):
        return f'<User {self.id}>'
