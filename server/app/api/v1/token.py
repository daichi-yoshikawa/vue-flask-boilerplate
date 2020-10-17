from flask import jsonify, make_response, request
from flask_jwt_extended create_access_token, craete_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_refresh_token_required, jwt_required
from flask_restful import Resource
from http import HTTPStatus
from werkzeug.security import generate_password_hash, check_password_hash


class TokenAPI(Resource):
  @jwt_required
  def get(self):
    status = HTTPStatus.OK
    ret = {}

    try:
      pass
    except Exception as e:
      status = HTTPStatus.UNAUTHORIZED
      ret = {
        'error': {
          'message': str(e),
        }
      }

    return make_response(jsonify(ret), status)

  def post(self):
    status = HTTPStatus.OK
    ret = {}

    try:
      data = request.get_json()
      user = User.query.filter_by(email=data['email']).first()

      if user is None:
        status = HTTPStatus.NOT_FOUND
        raise Exception('User was not found.')
      elif not check_password(user.password, data['password']):
        status = HTTPStatus.UNAUTHORIZED
        raise Exception('Password was wrong.')

      access_token = create_access_token(identity=user.id)
      refresh_token = create_refresh_token(identity=user.id)

      ret = {
        'access_token': access_token,
        'refresh_token': refresh_token,
      }
    except Exception as e:
      ret = {
        'error': {
          'message': str(e),
        },
      }

      if status == HTTPStatus.OK:
        status = HTTPStatus.BAD_REQUEST
        ret['error']['message'] = 'Bad request was sent.'

    return make_response(jsonify(ret), status)

  def delete(self):
    print('Logout')

  @jwt_refresh_token_required
  def put(self):
    status = HTTPStatus.OK
    ret = {}

    try:
      identity = get_jwt_identity()
      access_token = create_access_token(identity=identity)
      ret = {
        'access_token': access_token,
      }
    except Exception as e:
      status = HTTPStatus.UNAUTHORIZED
      ret = {
        'error': {
          'message': str(e),
        },
      }

    return make_response(jsonify(ret), status)
