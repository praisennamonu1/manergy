# This imports the required models and classes
from slugify import slugify
from uuid import uuid4
import random
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy

# start the connection to the database
db = SQLAlchemy()


# Implement base model here
class Base(db.Model):
    """Serve as the starting point for every model."""

    __abstract__ = True

    id = db.Column(db.String(128), primary_key=True,
                   default=lambda: uuid4().hex)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    slugname = db.Column(db.String(255))
    
    @classmethod
    def get_all(cls):
        """Return all the records in the table represented by the model."""
        return cls.query.all()
    
    @classmethod
    def get_one_by(cls, **attrs):
        """Get a record by given attributes."""
        return cls.query.filter_by(**attrs).first()
    
    @classmethod
    def get_count(cls, **kwargs):
        """Count records that satisfy the condition passed."""
        query = cls.query

        if kwargs:
            query.filter_by(**kwargs)
        return query.count()
    
    @classmethod
    def get_by_order(cls, *args):
        """Return all the records in a table ordered by given args."""
        return cls.query.order_by(*args).all()
    
    @classmethod
    def get_random(cls):
        """Return a random record from the table."""
        all_records = cls.all()
        random_idx = random.randint(0, len(all_records) - 1)
        # return a random record
        return all_records[random_idx]
    
    @classmethod
    def get_latest(cls, count=1):
        """Return the first record in a table order by created_by (desc)."""
        return cls.query.order_by(cls.created_at.desc()
                                  ).limit(count).all()
    
    @classmethod
    def get_by_id(cls, _id):
        """Return a record that satifies the given id or None if not found."""
        return cls.query.get(_id)
    
    @classmethod
    def get_by_slug(cls, slugname):
        """Return a record that satifies the given slug."""
        return cls.query.filter_by(slugname=slugname).first()
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def rollback(self):
        db.session.rollback()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    # utilities methods
    @staticmethod
    def sluggy(string):
        """Turns a string into a slug."""
        slug = slugify(string)

        if len(slug) > 255:
            raise ValueError('The string provided exceeds the maximum of 255.')
        return slug
