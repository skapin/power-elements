import logging

from flask import request, jsonify, abort, Blueprint
from flask_restful import Resource, reqparse
from common.utils.security import generate_user_token
from db.models import Account
from common.db.base import Database
from flask_restful_swagger import swagger


LOG = logging.getLogger(__name__)

PARSER = reqparse.RequestParser()
PARSER.add_argument('username')
PARSER.add_argument('password')

class Login(Resource):
    @swagger.operation(
        notes='Route to login existing customer',
        parameters=[
            {
              "name": "user",
              "description": "Username for the new account",
              "required": True,
              "allowMultiple": False,
              "dataType": "string"
            },
            {
              "name": "password",
              "description": "Password for the new account",
              "required": True,
              "allowMultiple": False,
              "dataType": "string"
            }
        ],
        responseMessages=[
            {
              "code": 200,
              "message": "Everything went right"
            },
            {
              "code": 415,
              "message": "Missing parameters"
            },
            {
              "code": 404,
              "message": "No account found"
            },
            {
              "code": 403,
              "message": "Incorrect password"
            }
        ]
    )
    def post(self):
        params = PARSER.parse_args()
        if not params:
            abort(415)

        username = params.get('username', False)
        password = params.get('password', False)
        account = False
        with Database(auto_commit=True) as db:
            account = db.query(Account).filter_by(name=username).first()
            if not account:
                abort(404)
            if not account.check_password(password):
                abort(403)

            return jsonify(login=True, token=generate_user_token(account.get_data()).decode('utf8'), username=username)