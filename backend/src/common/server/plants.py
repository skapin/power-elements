# coding: latin-1
from flask_restful import Resource, reqparse
from common.db.tools import to_dict, serialize
from common.db import models
from common.server.flaskutils import abort_doesnt_exist


class PlantView(Resource):
    def get(self, xid):
        plant = models.Plant.query.filter_by(uniqid=xid).first()
        abort_doesnt_exist(plant)

        return serialize(to_dict(plant))


parser = reqparse.RequestParser()
parser.add_argument('customer')
parser.add_argument('plant')


class PlantListView(Resource):

    def post(self):
        list_workstations = []
        list_sessions = []
        list_line = []
        returnDict = {'list_sessions': ' ',
                      'list_workstations': ' ',
                      'list_lines': ' '}

        args = parser.parse_args()
        name_customer = args.customer
        name_plant = args.plant

        workstations = models.Workstation.query.order_by(models.Workstation.name.asc())\
                                         .join(models.Line).order_by(models.Line.uniqid.asc())\
                                         .join(models.Plant).filter_by(name=name_plant)\
                                         .join(models.Customer).filter_by(name=name_customer).all()

        for w in workstations:
            list_workstations.append(serialize(to_dict(w)))

        for x in range(0, len(list_workstations)):
            session = models.Session.query.filter_by(workstation_id=list_workstations[x]['uniqid']).all()
            for s in session:
                list_sessions.append(serialize(to_dict(s)))

        for y in range(0, len(list_workstations)):
            line = models.Line.query.filter_by(uniqid=list_workstations[y]['line_id']).first()
            if(y % 10 == 0):
                list_line.append(serialize(to_dict(line)))

        returnDict['list_sessions'] = list_sessions
        returnDict['list_workstations'] = list_workstations
        returnDict['list_lines'] = list_line

        return returnDict
