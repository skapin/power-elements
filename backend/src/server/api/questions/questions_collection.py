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

class QuestionsCollection(Resource):
    @swagger.operation(
        notes='return all exising questions',
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
        return_list = []
        with Database(auto_commit=True) as db:
            questions = db.query(Question).all()
            for question in questions:
                return_list.append({'name': question.name, 'uniqid': question.uniqid})
        return jsonify(return_list)


    @swagger.operation(
        notes='remove all existing questions',
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
    def delete(self):
        with Database(auto_commit=True) as db:
            questions = db.query(Question).all()
            for question in questions:
                db.delete(question)
        return jsonify(True)
