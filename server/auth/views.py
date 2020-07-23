from flask import render_template
from . import auth_blueprint as auth


@auth.route('/login')
def login():
  return {'You implement': 'login page here if needed'}


@auth.route('/signup')
def signup():
  return {'You implement': 'signup page here if needed'}
