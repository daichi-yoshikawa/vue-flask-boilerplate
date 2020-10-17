import os
from flask import Flask

import models
from models.db import db, migrate
from api.authentication import jwt
from config import config


def get_flask_path(env):
  flask_root_path = os.getenv('FLASK_ROOT_PATH')
  if env == 'testing': # pytest is called in server dir.
    flask_root_path = '../client'

  root_path = os.path.abspath(flask_root_path)
  default_folder = 'dist/pro' if env == 'production' else 'dist/dev'

  template_folder = os.path.join(
    root_path, os.getenv('FLASK_TEMPLATE_DIR') or default_folder)
  static_folder = os.path.join(
    root_path, os.getenv('FLASK_STATIC_DIR') or default_folder)
  print('rootpath:', os.getenv('FLASK_ROOT_PATH'))
  print('rootpath:', root_path)

  return {
    'root_path': root_path,
    'template_folder': template_folder,
    'static_folder': static_folder,
  }


def create_app(testing=False):
  env = 'testing' if testing else os.getenv('FLASK_ENV') or None
  print('testing:', testing)
  if env is None:
    raise RuntimeError('FLASK_ENV is not set.')

  flask_path = get_flask_path(env)
  flask_app = Flask(
    __name__, root_path=flask_path['root_path'],
    template_folder=flask_path['template_folder'],
    static_folder=flask_path['static_folder'])

  flask_app.config.from_object(config[env])
  config[env].init_app(flask_app)

  db.init_app(flask_app)
  migrate.init_app(flask_app, db)
  jwt.init_app(flask_app)

  from main import main_blueprint
  flask_app.register_blueprint(main_blueprint, url_prefix='/')
  """If you create SaaS activate the follows."""
  from api import api_blueprint
  flask_app.register_blueprint(api_blueprint, url_prefix='/api')

  return flask_app
