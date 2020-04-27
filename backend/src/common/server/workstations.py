
from flask_restful import Resource, reqparse
from common.db.tools import to_dict, serialize
from common.db import models
from common.server.flaskutils import abort_doesnt_exist
from server.extensions import db


class WorkstationView(Resource):
    def get(self, id):
        workstation = models.Workstation.query.filter_by(uniqid=id).first()
        abort_doesnt_exist(workstation)

        return serialize(to_dict(workstation))

    def delete(self, id):
        workstation = models.Workstation.query.filter_by(uniqid=id).first()
        abort_doesnt_exist(workstation)
        db.workstation.delete(workstation)
        db.workstation.commit()

        return '', 204


parser = reqparse.RequestParser()
parser.add_argument('customer')
parser.add_argument('plant')
parser.add_argument('line')
parser.add_argument('workstation')


class WorkstationListView(Resource):
    def post(self):
        args = parser.parse_args()
        name_customer = args.customer
        name_plant = args.plant
        name_line = args.line
        name_workstation = args.workstation

        sessions = []
        if name_workstation:
            list_session = models.Session.query.order_by(models.Session.created_at.asc())\
                                               .join(models.Workstation).filter_by(name=name_workstation)\
                                               .join(models.Line,).filter_by(name=name_line)\
                                               .join(models.Plant).filter_by(name=name_plant)\
                                               .join(models.Customer,).filter_by(name=name_customer).all()
        else:
            list_session = models.Session.query.join(models.Workstation)\
                                               .join(models.Line,).filter_by(name=name_line)\
                                               .join(models.Plant).filter_by(name=name_plant)\
                                               .join(models.Customer,).filter_by(name=name_customer).all()

        for l in list_session:
            sessions.append(serialize(to_dict(l)))
        return sessions
