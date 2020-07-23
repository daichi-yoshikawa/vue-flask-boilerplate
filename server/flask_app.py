import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import models
from config import config


def get_flask_path(env):
  root_path = os.path.abspath(os.getenv('FLASK_ROOT_PATH') or '../client')
  default_folder = 'dist/pro' if env == 'production' else 'dist/dev'

  template_folder = os.path.join(
    root_path, os.getenv('FLASK_TEMPLATE_DIR') or default_folder)
  static_folder = os.path.join(
    root_path, os.getenv('FLASK_STATIC_DIR') or default_folder)

  return {
    'root_path': root_path,
    'template_folder': template_folder,
    'static_folder': static_folder,
  }


def create_app():
  env = os.getenv('FLASK_ENV') or 'development'

  flask_path = get_flask_path(env)
  flask_app = Flask(
    __name__, root_path=flask_path['root_path'],
    template_folder=flask_path['template_folder'],
    static_folder=flask_path['static_folder'])

  flask_app.config.from_object(config[env])
  config[env].init_app(flask_app)

  [db.init_app(flask_app) for db in models.dbs]
  with flask_app.app_context():
    for db in models.dbs:
      db.create_all()

  from main import main_blueprint
  flask_app.register_blueprint(main_blueprint, url_prefix='/')
  """If you create SaaS activate the follows."""
  #from auth import auth_blueprint
  #flask_app.register_blueprint(auth_blueprint, url_prefix='/auth')
  #from app import app_blueprint
  #flask_app.register_blueprint(app_blueprint, url_prefix='/app')
  #from api import api_blueprint
  #flask_app.register_blueprint(api_blueprint, url_prefix='/api')

  return flask_app
