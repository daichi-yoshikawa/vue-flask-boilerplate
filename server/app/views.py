from flask import render_template
from . import app_blueprint as app


@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')
