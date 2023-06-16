"""tar.py contains the Task and Routine models, hence the name."""

from .base import Base, db
from enum import Enum


class TaskStatus(Enum):
    """Provides the available list of statuses that are supported by tasks."""

    NOT_STARTED = 'Not Started'
    IN_PROGRESS = 'In Progress'
    COMPLETED = 'Completed'
    OVERDUE = 'Overdue'
    CANCELLED = 'Cancelled'


class RoutineOrGoalStatus(Enum):
    """Provides the available list of statuses that are supported by routines."""

    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    PAUSED = 'Paused'
    COMPLETED = 'Completed'
    ABANDONED = 'Abandoned'


class TaskPriority(Enum):
    """Specifies the priorities of tasks supported by this application."""

    LOW = 0
    NORMAL = 1
    HIGH = 2
    URGENT = 3


task_routine = db.Table('task_routine',
                        db.Column('task_id', db.String(128), db.ForeignKey(
                            'tasks.id'), primary_key=True),
                        db.Column('routine_id', db.String(128), db.ForeignKey(
                            'routines.id'), primary_key=True)
                        )


class Task(Base):
    """Represents a task."""

    __tablename__ = 'tasks'

    user_id = db.Column(db.String(128), db.ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    priority = db.Column(db.Integer, default=TaskPriority.LOW)
    energy_required = db.Column(db.Float(precision=2), nullable=False)
    energy_consumed = db.Column(db.Float(precision=2))
    time_required = db.Column(db.Time, nullable=False)
    time_consumed = db.Column(db.Time)
    deadline = db.Column(db.DateTime(timezone=True), nullable=False)
    status = db.Column(db.String(16), default=TaskStatus.NOT_STARTED)

    # relationships
    routines = db.relationship(
        'Routine', secondary=task_routine,
        primaryjoin='Task.id == task_routine.c.task_id',
        secondaryjoin='Routine.id == task_routine.c.routine_id',
        backref=db.backref('tasks', lazy='dynamic')
    )

    @property
    def status(self):
        return self.status

    @status.setter
    def status(self, s):
        statuses = TaskStatus.__members__.values()
        if s not in statuses:
            raise ValueError(f'Task status must be any of {list(statuses)}.')
        self.status = s


class Routine(Base):
    """Represent routines that will be created for users."""

    __tablename__ = 'routines'

    user_id = db.Column(db.String(128), db.ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    name = db.Column(db.String(128), unique=True, nullable=False)
    desc = db.Column(db.String(512), nullable=False)
    energy_required = db.Column(db.Float(precision=2), nullable=False)
    energy_consumed = db.Column(db.Float(precision=2))
    time_required = db.Column(db.Time, nullable=False)
    time_consumed = db.Column(db.Time)
    status = db.Column(db.String(16), default=RoutineOrGoalStatus.INACTIVE)

    @property
    def status(self):
        return self.status

    @status.setter
    def status(self, s):
        statuses = RoutineOrGoalStatus.__members__.values()
        if s not in statuses:
            raise ValueError(f'Routine status must be any of {list(statuses)}')
        self.status = s


class Goal(Base):
    """Represents the goals assigned to each routine or task."""
    user_id = db.Column(db.String(128), db.ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    name = db.Column(db.String(64), nullable=False, unique=True)
    desc = db.Column(db.String(512), nullable=False)
    deadline = db.Column(db.DateTime(timezone=True), nullable=False)
    status =  db.Column(db.String(16), default=RoutineOrGoalStatus.ACTIVE)

    @property
    def status(self):
        return self.status

    @status.setter
    def status(self, s):
        statuses = RoutineOrGoalStatus.__members__.values()
        if s not in statuses:
            raise ValueError(f'Routine status must be any of {list(statuses)}')
        self.status = s
