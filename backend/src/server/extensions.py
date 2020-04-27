# from flask_sqlalchemy import SQLAlchemy

import flask

from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_restful_swagger import swagger


db = SQLAlchemy()
cors = CORS()
rest_api = swagger.docs(Api(), apiVersion='0.1')
