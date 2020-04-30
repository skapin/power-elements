import logging
from flask import jsonify, Blueprint, abort
from server.extensions import rest_api
from server.api.auth.login import Login
from server.api.responses.responses_collection import ResponsesCollection
from server.api.questions.init_questions import InitQuestions
from server.api.questions.questions_collection import QuestionsCollection
from server.api.auth.signup import Signup
from common.utils.security import authentication_required
from common.db.base import Database
from db.models import Account, Response

LOG = logging.getLogger(__name__)

blueprint = Blueprint('views', __name__)

rest_api.add_resource(Login, '/api/users/login', methods=['POST'])
rest_api.add_resource(InitQuestions, '/api/questions/load', methods=['GET'])
rest_api.add_resource(QuestionsCollection, '/api/questions', methods=['GET', 'DELETE'])
rest_api.add_resource(Signup, '/api/users/signup', methods=['POST'])
rest_api.add_resource(ResponsesCollection, '/api/responses', methods=['POST'])


@blueprint.route('/status/is_up', methods=['GET'])
def is_up():
    return jsonify(is_up=True)


@blueprint.route('/api/user_info', methods=['DELETE'])
@authentication_required
def clear_user_info(user):
    with Database() as db:
        account = db.query(Account).filter_by(uniqid=user['uniqid']).first()
        if not account:
            abort(404, 'User not found')
        responses = db.query(Response).filter_by(account=account)

        for response in responses:
            db.delete(response)
        db.commit()
        db.delete(account)
        db.commit()

    return jsonify(is_up=True)
