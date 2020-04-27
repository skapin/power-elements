
from flask_restful import Resource
from common.db.tools import to_dict, serialize
from common.db import models

from common.server.flaskutils import abort_doesnt_exist


class CustomerView(Resource):
    def get(self, id):
        customer = models.Customer.query.filter_by(uniqid=id).first()
        abort_doesnt_exist(customer)

        return serialize(to_dict(customer))


class CustomerListView(Resource):
    def get(self):
        custs = []
        for c in models.Customer.query.all():
            custs.append(to_dict(c))
        return custs
