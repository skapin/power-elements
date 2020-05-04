import logging
import json

from flask import request, jsonify, abort, Blueprint
from flask_restful import Resource, reqparse
from config.settings import SETTINGS
from common.utils.security import generate_user_token, extract_payload
from db.models import Question, Account, Response
from common.db.base import Database
from flask_restful_swagger import swagger
from sqlalchemy import desc, func

LOG = logging.getLogger(__name__)

class Stats(Resource):
    @swagger.operation(
        notes='Get Stats from answers',
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
        return_list = []
        with Database(auto_commit=True) as db:

            questions_query = db.query(Question).all()

            for num, question in enumerate(questions_query):

                stats = db.query(Response)\
                  .join(Question)\
                  .join(Account)\
                  .filter(Response.question_id == question.uniqid)\
                  .all()

                answers = []
                for row in stats:
                    answers.append({'value': row.value,
                                    'created_at': row.created_at,
                                    'username': row.account.name
                                    })

                return_list.append({
                  'index': num,
                  'question_id': question.uniqid,
                  'question_name':question.name,
                  'results': answers

                })



        return jsonify(return_list)

    def get(self):
        with Database(auto_commit=True) as db:
            all_answers = db.query(func.date(Response.created_at), func.count(Response.value))\
                            .filter_by(value=100)\
                            .group_by(func.date(Response.created_at))\
                            .all()
            LOG.info(all_answers)
            return jsonify(all_answers)