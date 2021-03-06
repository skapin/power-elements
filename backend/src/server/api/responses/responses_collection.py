import logging
import json
import datetime


from flask import jsonify, abort
from flask_restful import Resource, reqparse
from common.utils.security import authentication_required
from db.models import Question, Account, Response
from common.db.base import Database
from flask_restful_swagger import swagger

LOG = logging.getLogger(__name__)
PARSER = reqparse.RequestParser()
PARSER.add_argument('responses')


class ResponsesCollection(Resource):
    @swagger.operation(
        notes='Save response inside DB',
        parameters=[
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
    @authentication_required
    def post(self, user):
        params = PARSER.parse_args()
        if not params:
            abort(415)

        responses = json.loads(params.get('responses', False))
        decoded_jwt = user
        today = datetime.datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)


        with Database(auto_commit=True) as db:
            account = db.query(Account).filter_by(uniqid=decoded_jwt['uniqid']).first()
            if not account:
                abort(404, 'User account not found')

            already_answered_today = db.query(Response).filter_by(account_id=decoded_jwt['uniqid']).filter(Response.created_at >= today).all()

            if already_answered_today:
                abort(403, 'Already answered today')

            for response in responses:
                reponse = responses[response]
                actual_question = db.query(Question).filter_by(name=reponse['question']).first()
                new_response = Response(int(reponse['value']), actual_question, account)
                db.add(new_response)
        return jsonify(False)

    @authentication_required
    def put(self, user):
        params = PARSER.parse_args()
        if not params:
            abort(415)

        responses = json.loads(params.get('responses', False))
        decoded_jwt = user
        today = datetime.datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)


        with Database(auto_commit=True) as db:
            account = db.query(Account).filter_by(uniqid=decoded_jwt['uniqid']).first()
            if not account:
                abort(404, 'User account not found')

            for response in responses:
                reponse = responses[response]
                actual_question = db.query(Question).filter_by(name=reponse['question']).first()

                current_response = db.query(Response)\
                    .filter_by(account_id=decoded_jwt['uniqid'])\
                    .filter(Response.created_at >= today)\
                    .filter_by(question_id=actual_question.uniqid)\
                    .first()
                
                current_response.value = int(reponse['value'])


        return jsonify("updated answer")
