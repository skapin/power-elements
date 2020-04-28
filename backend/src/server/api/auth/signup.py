import logging
import random

from flask import request, jsonify, abort, Blueprint
from flask_restful import Resource, reqparse
from common.utils.security import generate_user_token, hash_password
from db.models import Account
from common.db.base import Database
from flask_restful_swagger import swagger


LOG = logging.getLogger(__name__)

PARSER = reqparse.RequestParser()
PARSER.add_argument('password')

class Signup(Resource):
    @swagger.operation(
        notes='Route to add a new customer',
        parameters=[
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
              "code": 403,
              "message": "Username already existing"
            }
        ]
    )
    def post(self):
        params = PARSER.parse_args()
        if not params:
            abort(415)

        password = params.get('password', False)


        adjectiveList = ["Happy", "Silly", "Tiny", "Super", "Musical", "Funny"]
        colorList = ['Yellow', 'Pink', 'Green', 'Blue', 'Orange', 'Red']
        animalList = ['Elephant', 'Unicorn', 'Giraffe', 'Dinosaur', 'Kangaroo']
        adjective = random.choice(adjectiveList)
        color = random.choice(colorList)
        animal = random.choice(animalList)
        number = str(random.randint(1, 100))

        username = adjective + color + animal + number
        hash = hash_password(password)

        account = False

        with Database(auto_commit=True) as db:
            account = db.query(Account).filter_by(name=username).first()
            # if account:
            #     abort(403)
            new = Account(username, hash)
            db.add(new)
        return jsonify(Signup=True, Username=username, Password=password)