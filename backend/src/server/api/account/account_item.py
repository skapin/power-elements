import logging

from flask import request, jsonify, abort, Blueprint
from flask_restful import Resource, reqparse
from common.utils.security import generate_user_token, authentication_required
from db.models import Account
from common.db.base import Database
from flask_restful_swagger import swagger


LOG = logging.getLogger(__name__)

PARSER = reqparse.RequestParser()
PARSER.add_argument('value')

class AccountItem(Resource):
    @swagger.operation(
        notes='patch if user is here or not',
        parameters=[
            {
              "name": "user",
              "description": "user",
              "required": True,
              "allowMultiple": False,
              "dataType": "string"
            },
            {
              "name": "value",
              "description": "is here",
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
    @authentication_required
    def patch(self, user):
        params = PARSER.parse_args()
        if not params:
            abort(415)

        is_here = params.get('value', False)
        decoded_jwt = user
        with Database(auto_commit=True) as db:
            account = db.query(Account).filter_by(uniqid=decoded_jwt['uniqid']).first()
            if not account:
                abort(404, 'User account not found')
            account.at_work = bool(is_here)
            db.add(account)
        return jsonify(True)