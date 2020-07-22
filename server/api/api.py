from flask_restful import Resource

from . import api


@api.resource('/hello')
class HelloResource(Resource):
  def get(self):
    return {'Hello': 'RESTful API world'}



"""
@api.route('/', methods=['GET'])
def hello():
  return {'Hello': 'API world'}
"""
