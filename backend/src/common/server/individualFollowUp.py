
from flask_restful import Resource
from common.db.tools import to_dict, serialize
from common.db import models

from common.server.flaskutils import abort_doesnt_exist


class IndividualFollowUpView(Resource):
    def get(self, id):
        person = models.Person.query.filter_by(uniqid=id).first()
        abort_doesnt_exist(person)

        return serialize(to_dict(person))


class IndividualFollowUpListView(Resource):
    def post(self):
        pers = []
        for p in models.Person.query.all():
            pers.append(to_dict(p))
        return pers
