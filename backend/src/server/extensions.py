# from flask_sqlalchemy import SQLAlchemy

import flask

from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
cors = CORS()
rest_api = Api()
