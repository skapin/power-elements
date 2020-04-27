
from flask_restful import Resource
from common.db.tools import to_dict, serialize
from common.db import models
from server.extensions import db

from common.server.flaskutils import abort_doesnt_exist, flask_log


class NumiiView(Resource):
    def get(self, id):
        numii = models.Numii.query.filter_by(uniqid=id).first()
        abort_doesnt_exist(numii)

        return serialize(to_dict(numii))


class NumiiListView(Resource):
    def get(self):
        numiis = []
        numii = models.Numii.query.join(models.Customer)
        for n in numii:
            numiis.append(serialize(to_dict(n)))
        return numiis
