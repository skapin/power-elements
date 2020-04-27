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

LOG = logging.getLogger(__name__)

blueprint = Blueprint('views', __name__)

rest_api.add_resource(Login, '/api/users/login', methods=['POST'])

@blueprint.route('/status/is_up', methods=['GET'])
def is_up():
    return jsonify(is_up=True)
