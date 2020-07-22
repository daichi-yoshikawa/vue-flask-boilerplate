from flask_restful import Resource


class Sample(Resource):
  def get(self):
    return {'Hello': 'RESTful API world'}
