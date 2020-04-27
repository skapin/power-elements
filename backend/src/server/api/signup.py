import logging

from flask import request, jsonify, abort, Blueprint
from flask_restful import Resource, reqparse
from common.utils.security import generate_user_token, hash_password
from db.models import Account
from common.db.base import Database
from flask_restful_swagger import swagger


LOG = logging.getLogger(__name__)

PARSER = reqparse.RequestParser()
PARSER.add_argument('user')
PARSER.add_argument('password')

class Signup(Resource):
    @swagger.operation(
        notes='Route to add a new customer',
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
    def get(self):

        username = "test1"
        password = "azerty"
        hash = hash_password(password)
        account = False
        with Database(auto_commit=True) as db:
            account = db.query(Account).filter_by(name=username).first()
            if account:
                abort(403)
            new = Account(username, hash)
            db.add(new)


        return jsonify(Signup=True, Username=username, Password=password)