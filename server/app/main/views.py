from flask import render_template
from . import main_blueprint as main


@main.route('/', methods=['GET'])
def main_index():
  return render_template('index.html')
