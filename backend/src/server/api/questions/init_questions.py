import logging
import csv

from flask import request, jsonify, abort, Blueprint
from flask_restful import Resource, reqparse
from config.settings import SETTINGS
from common.utils.security import generate_user_token
from db.models import Question
from common.db.base import Database
from flask_restful_swagger import swagger

LOG = logging.getLogger(__name__)

class InitQuestions(Resource):
    @swagger.operation(
        notes='Load qcm inside db',
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
    def get(self):
        path_to_file = SETTINGS['QUESTIONS_FILE']

        if not path_to_file:
            abort(405)
        with Database(auto_commit=True) as db:
            with open(path_to_file, 'r') as csvfile:
                qcm = csv.DictReader(csvfile, delimiter=',', quotechar='"', restval=90)
                for question in qcm:
                    question_already_here = db.query(Question).filter_by(name=question['Question']).first()
                    if question_already_here:
                        LOG.info('QUESTION ALREADY IN DB.... moving on')
                        continue
                    tmp_question = Question(question['Question'])
                    # tmp_question = Question(question['Question'], question['Ressource'], QCM)
                    db.add(tmp_question)
        return jsonify(loaded=True)
