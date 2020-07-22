from flask import Blueprint
from flask_restful import Api

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

"""
Do not create api.py under api dir and import api here,
because "api" is already reserved for an instance of Blueprint.
"""
from .sample import Sample

api.add_resource(Sample, '/sample')
