from .base import Base, db
from flask_login import UserMixin, AnonymousUserMixin
from flask import current_app
from ..common.error_classes import RestrictionError
from werkzeug.security import generate_password_hash, check_password_hash


class Permission:
    VIEW_TASKS = 1
    CREATE_TASKS = 2
    EDIT_TASKS = 4
    DELETE_TASKS = 8
    VIEW_ROUTINES = 16
    CREATE_ROUTINES = 32
    EDIT_ROUTINES = 64
    DELETE_ROUTINES = 126
    VIEW_USERS = 256
    EDIT_USERS = 512
    DELETE_USERS = 1024
    ADMIN = 2048


class Role(Base):
    """Describes the roles that a user can have."""

    __tablename__ = 'roles'

    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions -= perm

    def reset_permissions(self):
        self.permissions = 0

    def has_permission(self, perm):
        return self.permissions & perm == perm

    @staticmethod
    def insert_roles():
        roles = {
            'User': [
                Permission.VIEW_TASKS, Permission.CREATE_TASKS,
                Permission.EDIT_TASKS, Permission.DELETE_TASKS
            ],
            'Manager': [
                Permission.VIEW_TASKS, Permission.CREATE_TASKS,
                Permission.EDIT_TASKS, Permission.DELETE_TASKS,
                Permission.CREATE_ROUTINES, Permission.EDIT_ROUTINES,
                Permission.DELETE_ROUTINES, Permission.VIEW_USERS,
                Permission.EDIT_USERS
            ],
            'Administrator': [
                Permission.VIEW_TASKS, Permission.CREATE_TASKS,
                Permission.EDIT_TASKS, Permission.DELETE_TASKS,
                Permission.CREATE_ROUTINES, Permission.EDIT_ROUTINES,
                Permission.DELETE_ROUTINES, Permission.VIEW_USERS,
                Permission.EDIT_USERS, Permission.DELETE_USERS,
                Permission.ADMIN
            ]
        }
        default_role = 'User'
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if not role:
                role = Role(name=r)
            role.reset_permissions()
            for perm in roles[r]:
                role.add_permission(perm)
            role.default = (role.name == default_role)
            # save role
            db.session.add(role)
        db.session.commit()


class User(UserMixin, Base):
    """Represent the blueprint for all users."""

    __tablename__ = 'users'

    firstname = db.Column(db.String(64), nullable=False)
    lastname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    hashed_password = db.Column(db.String(128))
    birth_date = db.Column(db.Date())
    gender = db.Column(db.String(16))
    occupation = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    # relationships
    tasks = db.relationship('Task', backref='user', lazy='dynamic')
    routines = db.relationship('Routine', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise RestrictionError()

    @password.setter
    def password(self, p):
        self.hashed_password = generate_password_hash(p, salt_length=15)

    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'
    
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.email in current_app.config['ADMIN_LIST']:
                self.role = Role.get_one_by(name='Administrator')
            if self.role is None:
                self.role = Role.get_one_by(default=True)

    def verify_password(self, password):
        """Verify that the password passed is valid and correct."""
        return check_password_hash(self.hashed_password, password)
    
    def can(self, perm):
        return self.role is not None and self.role.has_permission(perm)
    
    def is_admin(self):
        return self.can(Permission.ADMIN)


class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_admin(self):
        return False
