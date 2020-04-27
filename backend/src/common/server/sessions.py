
from flask_restful import Resource, reqparse
from common.db.tools import to_dict, serialize, serialize_foreign
from common.db import models
from server.extensions import db
from common.server.flaskutils import abort_doesnt_exist, flask_log
from datetime import datetime


class SessionView(Resource):
    def get(self, id):
        session = models.Session.query.filter_by(uniqid=id).first()
        abort_doesnt_exist(session)

        return serialize(to_dict(session))

    def patch(self, id):
        session = models.Session.query.filter_by(uniqid=id).first()
        session.tagged = True
        db.session.commit()

    def delete(self, id):
        session = models.Session.query.filter_by(uniqid=id).first()
        abort_doesnt_exist(session)
        db.session.delete(session)
        db.session.commit()


class SessionListView(Resource):
    def get(self):
        sessions = []
        for s in models.Session.query.order_by(
                models.Session.start_at.desc()).limit(10):
            d = to_dict(s)
            d.update(serialize_foreign(s, 'observator', ['hash']))
            d.update(serialize_foreign(s, 'worker', ['hash']))
            d.update(serialize_foreign(s, 'workstation'))
            sessions.append(serialize(d))
        return sessions


parser = reqparse.RequestParser()
parser.add_argument('prosDate')


class SessionListViewSinceLastSync(Resource):
    def post(self):
        # handle parameter from client
        args = parser.parse_args()
        pros_date = args.prosDate

        # get data from db based on parameter since last sync
        sessions = models.Session.query.filter(models.Session.created_at >= pros_date).all()

        nbr_session = 0
        session_duration = 0

        for s in sessions:
            if s.end_at is not None:
                session_duration += (s.end_at - s.start_at).total_seconds()
                nbr_session += 1

        return {'nb_session': nbr_session, 'session_duration': session_duration}
        # in ms
