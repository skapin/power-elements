
from flask_restful import Resource, reqparse
from common.db.tools import to_dict, serialize, serialize_foreign
from common.db import models
from server.extensions import db

parser_list = reqparse.RequestParser()
parser_list.add_argument('fromx', type=int)
parser_list.add_argument('to', type=int)

class LabellisationListView(Resource):
    def post(self):
        nonLabelledSessions = []
        args = parser_list.parse_args()
        fromx = args.fromx if args.fromx else 0
        to = args.to if args.to else 10

        sessions = models.Session.query.filter_by(tagged=False).order_by(models.Session.start_at.desc()).limit(100)
        # to = len(sessions) if len(sessions) < to else to
        # fromx = len(sessions) if len(sessions) < fromx else fromx
        # sessions = session[fromx, to]

        for s in sessions:
            d = to_dict(s)
            d.update(serialize_foreign(s, 'observator', ['hash']))
            d.update(serialize_foreign(s, 'worker', ['hash']))
            d.update(serialize_foreign(s, 'workstation'))
            nonLabelledSessions.append(serialize(d))
        return nonLabelledSessions


parser = reqparse.RequestParser()
parser.add_argument('sessionID')


class LabellisationSetTaggedTrue(Resource):
    def post(self):
        args = parser.parse_args()
        session_id = args.sessionID

        session = models.Session.query.filter_by(uniqid=session_id).first()
        session.tagged = True
        db.session.commit()
        return True
