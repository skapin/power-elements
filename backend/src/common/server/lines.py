
from flask_restful import Resource, reqparse
from common.db.tools import to_dict, serialize
from common.db import models
from common.server.flaskutils import abort_doesnt_exist


class LineView(Resource):
    def get(self, id):
        line = models.Line.query.filter_by(uniqid=id).first()
        abort_doesnt_exist(line)

        return serialize(to_dict(line))


parser = reqparse.RequestParser()
parser.add_argument('customer')
parser.add_argument('plant')
parser.add_argument('line')


class LineListView(Resource):
    def post(self):
        args = parser.parse_args()
        name_customer = args.customer
        name_plant = args.plant
        name_line = args.line

        workstations = []
        list_workstations = models.Workstation.query.join(models.Line).filter_by(name=name_line).order_by(models.Line.name.asc())\
                                                    .join(models.Plant).filter_by(name=name_plant)\
                                                    .join(models.Customer).filter_by(name=name_customer).all()

        for l in list_workstations:
            workstations.append(serialize(to_dict(l)))
        return workstations
