from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from config.settings import SETTINGS
from psycopg2 import IntegrityError as PgIntegrityError
from sqlalchemy.exc import IntegrityError as SQLIntegrityError
from common.server.flaskutils import print_flush

ENGINE = create_engine("postgresql+psycopg2://" + SETTINGS['POSTGRES_USER'] + ":" +
                       SETTINGS['POSTGRES_PASSWORD'] + '@' + SETTINGS['POSTGRES_HOST'] + ':' +
                       SETTINGS['POSTGRES_PORT'] + '/' + SETTINGS['POSTGRES_DB'])
# use session_factory() to get a new Session
_SessionFactory = scoped_session(sessionmaker(bind=ENGINE))

Base = declarative_base()

# not used
# http://flask.pocoo.org/snippets/22/
# http://docs.sqlalchemy.org/en/latest/orm/contextual.html
# def init_engine(uri, **kwargs):
#     global ENGINE
#     ENGINE = create_engine("postgresql+psycopg2://" + SETTINGS['POSTGRES_USER'] + ":" +
#                        SETTINGS['POSTGRES_PASSWORD'] + '@' + SETTINGS['POSTGRES_HOST'] + ':' +
#                        SETTINGS['POSTGRES_PORT'] + '/' + SETTINGS['POSTGRES_DB'])
#     return ENGINE


def commit_ignore_integrity(db, details=''):
    try:
        print_flush('[NEW REF]   ' + details)
        db.commit()
    except PgIntegrityError as e:
        print_flush('[WARNING] Duplicate entry for kanban ref. All stop.' + str(e))
        db.rollback()
        return False
    except SQLIntegrityError as e:
        print_flush('[WARNING] Duplicate entry for kanban ref. All stop.' + str(e))
        db.rollback()
        return False
    else:
        return True


class Database():

    @staticmethod
    def drop_all():
        Base.metadata.drop_all(ENGINE)

    def __init__(self, auto_commit=False, create_all=False):
        self.auto_commit = auto_commit
        self.session_factory = session_factory()

        if create_all:
            Base.metadata.create_all(ENGINE)

    def __enter__(self):
        return self.session_factory

    def __exit__(self, type, value, traceback):
        if self.auto_commit:
            self.session_factory.commit()
        self.session_factory.flush()
        self.session_factory.close()


def session_factory():
    # Base.metadata.create_all(ENGINE)
    return _SessionFactory()
