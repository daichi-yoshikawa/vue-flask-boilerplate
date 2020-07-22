from flask import Blueprint

app_blueprint = Blueprint('app', __name__)

from . import views
