from .. import db
from .base import Base
from enum import Enum


class TaskPriority(Enum):
    """Specifies the priorities of tasks supported by this application."""

    LOW = 1
    HIGH = 2
    URGENT = 3


class Task(Base):
    """Represents a task."""

    __tablename__ = 'tasks'

    user_id = db.Column(db.String(128), db.ForeignKey(
        'users.id', ondelete='CASCADE'), unique=True)
    name = db.Column(db.String(64), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    priority = db.Column(db.Integer, default=TaskPriority.LOW)
