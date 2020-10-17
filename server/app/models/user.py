from datetime import datetime
from sqlalchemy import func
from sqlalchemy.sql import expression

from .db import db


class User(db.Model):
  name = 'users'
  __tablename__ = 'users'
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(128), unique=True, nullable=False)
  email = db.Column(db.String(128), unique=True, nullable=False)
  password = db.Column(db.String(128), unique=False, nullable=False)
  agreed_eula = db.Column(db.Boolean, nullable=False, server_default=expression.false())
  created_on = db.Column(db.DateTime(), server_default=func.now())
  updated_on = db.Column(db.DateTime(), server_default=func.now(), server_onupdate=func.now())

  def __repr__(self):
    return f'User(id={self.id}, ' +\
           f'name={self.name}, ' +\
           f'email={self.email}, ' +\
           f'eula={self.agreed_eula})'

