from flask import render_template
from . import app_blueprint as app


@app.route('/', methods=['GET'])
def app_index():
  return {'If user login,': 'this page may be index.'}
