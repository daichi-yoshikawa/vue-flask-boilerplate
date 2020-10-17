from flask import jsonify, make_response, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from http import HTTPStatus
from werkzeug.security import generate_password_hash


from models.db import db
from models.user import User


class UserListAPI(Resource):
  def get(self):
    return make_response(jsonify({'test': 'value'}), 200)

  def post(self):
    status = HTTPStatus.CREATED
    ret = {}

    try:
      data = request.get_json()
      exists = User.query.filter_by(email=data['email']).first()

      if exists:
        status = HTTPStatus.OK
        data.pop('password')
        return make_response(jsonify(data), status)

      data['password'] = generate_password_hash(data['password'])

      user = User(**data)
      db.session.add(user)
      db.session.commit()

      user = User.query.filter_by(email=data['email']).first()
      data.pop('password')
      ret = data
    except Exception as e:
      db.session.rollback()

      ret = {
        'error': {
          'message': str(e),
        },
      }

      if status == HTTPStatus.CREATED:
        status = HTTPStatus.INTERNAL_SERVER_ERROR
        ret['error']['message'] = 'Internal server error occurred.'

    return make_response(jsonify(ret), status)


class UserAPI(Resource):
  @jwt_required
  def get(self, id_):
    status = HTTPStatus.OK
    ret = {}

    try:
      query = db.session.query(User.name, User.email).filter(User.id == id_)
      user = query.first()
    except Exception as e:
      status = HTTPStatus.INTERNAL_SERVER_ERROR
      ret = {
        'error': {
          'message': str(e),
        },
      }
