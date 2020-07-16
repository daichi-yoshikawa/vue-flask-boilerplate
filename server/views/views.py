from flask import render_template

from app import app


@app.route('/', methods=['GET'])
def base():
  return render_template('index.html')
