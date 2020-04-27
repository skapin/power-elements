import logging
import decimal
import sentry_sdk
import enum

from flask import Flask
from flask.json import JSONEncoder
from server.extensions import cors, rest_api, db
from server import views, commands
from config.settings import SETTINGS
from common.server.flaskutils import init_logging
from datetime import date
from sentry_sdk.integrations.flask import FlaskIntegration


LOG = logging.getLogger(__name__)


class CustomJSONEncoder(JSONEncoder):

    def default(self, obj):
        try:
            if isinstance(obj, date):
                return obj.isoformat()
            if isinstance(obj, decimal.Decimal):
                return int(obj)
            if isinstance(obj, enum.Enum):
                return obj.value
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


def create_app(config_object=None):
    app = Flask(__name__.split('.')[0])
    app.json_encoder = CustomJSONEncoder
    app.config.from_object(config_object)
    init_logging()
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://" + SETTINGS['POSTGRES_USER'] + ":" + \
        SETTINGS['POSTGRES_PASSWORD'] + '@' + SETTINGS['POSTGRES_HOST'] + \
        ':' + SETTINGS['POSTGRES_PORT'] + '/' + SETTINGS['POSTGRES_DB']

    # sentry_sdk.init(
    #     dsn=SETTINGS['SENTRY_DSN'],
    #     integrations=[FlaskIntegration()]
    # )

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    return app


def register_extensions(app):
    cors.init_app(app)
    rest_api.init_app(app)
    db.init_app(app)

    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(views.blueprint)

    return None


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.create_all)
    app.cli.add_command(commands.drop_all)
