import json
import logging
import traceback
import datetime
import re
import requests

from config.settings import SETTINGS
from flask import request, jsonify, abort, Blueprint, send_file
from server import *
from server.extensions import rest_api

LOG = logging.getLogger(__name__)

blueprint = Blueprint('views', __name__)
# rest_api.add_resource(image_view.ImageView, '/cam_image')
# rest_api.add_resource(image_view.ImageSettings, '/image_settings')

@blueprint.route('/status/is_up', methods=['GET'])
def is_up():
    return jsonify(is_up=True)
