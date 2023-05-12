from .base import Base, db


class Achievement(Base):
    """Serve as a blueprints for achievements such as goal and routine completion."""

    __tablename__ = 'achievements'

    user_id = db.Column(db.String(128), db.ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    name = db.Column(db.String(32), nullable=False)
    desc = db.Column(db.String(128))


class Feedback(Base):
    """Represent a user's feedback."""

    user_id = db.Column(db.String(128), db.ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    task_id = db.Column(db.String(128), db.ForeignKey(
        'tasks.id', ondelete='CASCADE'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(256))
