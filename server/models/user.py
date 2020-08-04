from datetime import datetime

from .db import db


class User(db.Model):
  name = 'users'
  __tablename__ = 'users'
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(128), unique=True, nullable=False)
  email = db.Column(db.String(128), unique=True, nullable=False)
  password = db.Column(db.String(128), unique=False, nullable=False)
  created_at = db.Column(db.DateTime(), default=datetime.utcnow)
  updated_at = db.Column(db.DateTime(), default=datetime.utcnow)

  def __repr__(self):
    return f"User {self.id} : {self.name} created at {self.created_at}"
