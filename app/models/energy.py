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

    __tablename__ = 'feedbacks'

    user_id = db.Column(db.String(128), db.ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    task_id = db.Column(db.String(128), db.ForeignKey(
        'tasks.id', ondelete='CASCADE'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(256))


class Video(Base):
    """Represents a video uploaded for the users."""

    __tablename__ = 'videos'

    user_id = db.Column(db.String(128), db.ForeignKey(
        'users.id', ondelete='SET NULL'), nullable=True)
    thumbnail = db.Column(db.String(256))
    url = db.Column(db.String(256), nullable=False, unique=True)
    title = db.Column(db.String(128), nullable=False)
    desc = db.Column(db.String(512))
    duration = db.Column(db.Integer)  # in seconds
    keyword = db.Column(db.String(32), default='Mental Energy')
