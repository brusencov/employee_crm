from datetime import datetime

from config import db


class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    # @TODO User one-to-many relationship
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)

    def __repr__(self):
        return f'<Attendance {self.id}>'
