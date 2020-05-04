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

class AtWork(Resource):
    @swagger.operation(
        notes='Get Stats from account',
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
        with Database(auto_commit=True) as db:
            at_work_account = db.query(func.count(Account.uniqid)).filter_by(at_work=True).first()
            at_home_account = db.query(func.count(Account.uniqid)).filter_by(at_work=False).first()
            return jsonify({'at_work_account': at_work_account[0], 'at_home_account': at_home_account[0]})
