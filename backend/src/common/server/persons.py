
from flask_restful import Resource
from common.db.tools import to_dict, serialize
from common.db import models
from common.server.flaskutils import abort_doesnt_exist


class PersonListView(Resource):
    def get(self):
        users = []
        for c in models.Person.query.all():
            users.append(serialize(to_dict(c), ignore=['hash']))
        return users


class PersonView(Resource):
    def get(self, id):
        user = models.Person.query.filter_by(uniqid=id).first()
        abort_doesnt_exist(user)

        return serialize(to_dict(user), ignore=['hash'])
