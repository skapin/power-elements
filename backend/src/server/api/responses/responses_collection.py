import logging
import csv

from flask import request, jsonify, abort, Blueprint
from flask_restful import Resource, reqparse
from config.settings import SETTINGS
from common.utils.security import generate_user_token, extract_payload
from db.models import Question, Account, Response
from common.db.base import Database
from flask_restful_swagger import swagger

LOG = logging.getLogger(__name__)
PARSER = reqparse.RequestParser()
PARSER.add_argument('responses')
PARSER.add_argument('jwt')

class ResponsesCollection(Resource):
    @swagger.operation(
        notes='Save response inside DB',
        parameters=[
            {
              "name": "jwt",
              "description": "jwt to retrieve account",
              "required": True,
              "allowMultiple": False,
              "dataType": "string"
            },
            {
              "name": "responses",
              "description": "dict that contains answer for every questions",
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
              "code": 405,
              "message": "file not found"
            }
        ]
    )
    def post(self):
        params = PARSER.parse_args()
        if not params:
            abort(415)

        responses = params.get('responses', False)
        decoded_jwt = extract_payload(params.get('jwt', False))
        with Database(auto_commit=True) as db:
            account = db.query(Account).filter_by(uniqid=decoded_jwt['uniqid']).first()
            for response in responses:
                actual_question = db.query(Question).filter_by(name=response['question']).first()
                new_response = Response(response['value'], actual_question, account)
                db.add(new_response)
        return jsonify(True)