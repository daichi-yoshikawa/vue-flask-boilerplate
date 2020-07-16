import os
from flask import Flask
from config import config


env = os.getenv('FLASK_ENV') or 'development'
root_path = os.path.abspath(os.getenv('FLASK_ROOT_PATH') or '../client')

template_dir = os.getenv('FLASK_TEMPLATE_DIR') or\
               ('dist/pro' if env == 'production' else 'dist/dev')
template_path = os.path.join(root_path, template_dir)
static_dir = os.getenv('FLASK_STATIC_DIR') or\
             ('dist/pro' if env == 'production' else 'dist/dev')
static_path = os.path.join(root_path, static_dir)

app = Flask(
    __name__, template_folder=template_path,
    static_folder=static_path, root_path=root_path)


def create_app():
  app.config.from_object(config[env])
  config[env].init_app(app)

  import views
  import models
  import controllers

  return app
