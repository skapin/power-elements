
from flask_restful import Resource
from common.db.tools import to_dict, serialize, serialize_foreign
from common.db import models


class WebdataconnectorView(Resource):
    def get(self):
        sessions = []
        for s in models.Session.query.all():
            d = to_dict(s)
            d.update(serialize_foreign(s, 'observator', ['hash']))
            d.update(serialize_foreign(s, 'worker', ['hash']))
            d.update(serialize_foreign(s, 'workstation'))
            sessions.append(serialize(d))
        return sessions
