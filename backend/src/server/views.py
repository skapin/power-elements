import json
import logging
import traceback
import datetime
import re
import requests

from config.settings import SETTINGS
from flask import request, jsonify, abort, Blueprint, send_file
from server.extensions import rest_api

from server.api.login import Login
from server.api.questions.init_questions import InitQuestions
from server.api.questions.questions_collection import QuestionsCollection
from server.api.signup import Signup

LOG = logging.getLogger(__name__)

blueprint = Blueprint('views', __name__)

rest_api.add_resource(Login, '/api/users/login', methods=['POST'])
rest_api.add_resource(InitQuestions, '/api/questions/load', methods=['GET'])
rest_api.add_resource(QuestionsCollection, '/api/questions', methods=['GET', 'DELETE'])
rest_api.add_resource(Signup, '/api/users/signup', methods=['GET'])

@blueprint.route('/status/is_up', methods=['GET'])
def is_up():
    return jsonify(is_up=True)
