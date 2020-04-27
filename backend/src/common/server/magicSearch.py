
from flask_restful import Resource, reqparse
from common.db.tools import to_dict, serialize
from common.db import models
from common.server.flaskutils import abort_doesnt_exist, flask_log


class MagicSearchView(Resource):
    def get(self, id):
        session = models.Session.query.filter_by(uniqid=id).first()
        abort_doesnt_exist(session)

        return serialize(to_dict(session))


parser = reqparse.RequestParser()
parser.add_argument('message')


class MagicSearchListView(Resource):
    def post(self):
        message = ' '
        customer = []
        plant = []
        line = []
        workstation = []
        words = []
        list_customer = []
        list_plant = []
        list_line = []
        list_workstation = []

        returnDict = {'list_customer': ' ',
                      'list_plant': ' ',
                      'list_lines': ' ',
                      'list_workstation': ' '
                      }

        args = parser.parse_args()
        message = args.message
        words = message.split()

        # .encode c'est degueu faut changer ca
        for w in words:
            customer.append(models.Customer.query.filter_by(name=w.encode('ascii', 'ignore')).all())
            plant.append(models.Plant.query.filter_by(name=w.encode('ascii', 'ignore')).all())
            line.append(models.Line.query.filter_by(name=w.encode('ascii', 'ignore')).all())
            workstation.append(models.Workstation.query.filter_by(name=w.encode('ascii', 'ignore')).all)

        for c in customer:
            if c:
                list_customer.append(serialize(to_dict(c[0])))

        for p in plant:
            if p:
                list_plant.append(serialize(to_dict(p[0])))

        for l in line:
            if l:
                list_line.append(serialize(to_dict(l[0])))

        for w in workstation:
            if w:
                list_workstation.append(serialize(to_dict(w[0])))

        returnDict['list_customer'] = list_customer
        returnDict['list_plant'] = list_plant
        returnDict['list_line'] = list_line
        returnDict['list_workstation'] = list_workstation
        return returnDict
