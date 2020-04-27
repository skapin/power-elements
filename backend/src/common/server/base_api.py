from flask import Blueprint
from server.extensions import rest_api
from common.server import *


blueprint = Blueprint('base_api', __name__)


rest_api.add_resource(webdataconnector.WebdataconnectorView, '/api/webdataconnector')

rest_api.add_resource(customers.CustomerListView, '/api/customers')
rest_api.add_resource(customers.CustomerView, '/api/customers/<id>')

rest_api.add_resource(numiis.NumiiListView, '/api/numiis')
rest_api.add_resource(numiis.NumiiView, '/api/numii/<id>')

rest_api.add_resource(labellisation.LabellisationListView, '/api/labellisation')
rest_api.add_resource(labellisation.LabellisationSetTaggedTrue, '/api/setTaggedTrue')

rest_api.add_resource(magicSearch.MagicSearchListView, '/api/magicSearch')
rest_api.add_resource(magicSearch.MagicSearchView, '/api/magicSearch/<id>')

rest_api.add_resource(individualFollowUp.IndividualFollowUpListView, '/api/individualFollowUp')
rest_api.add_resource(individualFollowUp.IndividualFollowUpView, '/api/individualFollowUp/<id>')

rest_api.add_resource(plants.PlantListView, '/api/plants')
rest_api.add_resource(plants.PlantView, '/api/plants/<id>')

rest_api.add_resource(lines.LineListView, '/api/lines')
rest_api.add_resource(lines.LineView, '/api/lines/<id>')

rest_api.add_resource(workstations.WorkstationListView, '/api/workstations')
rest_api.add_resource(workstations.WorkstationView, '/api/workstations/<id>')

rest_api.add_resource(sessions.SessionListView, '/api/sessions')
rest_api.add_resource(sessions.SessionListViewSinceLastSync, '/api/sessionsListSinceLastSync')
rest_api.add_resource(sessions.SessionView, '/api/sessions/<id>')

rest_api.add_resource(persons.PersonListView, '/api/persons')
rest_api.add_resource(persons.PersonView, '/api/persons/<id>')

rest_api.add_resource(tags.TagListView, '/api/tags')
rest_api.add_resource(tags.TagView, '/api/tags/<id>')
rest_api.add_resource(tags.TagSearch, '/api/tags/search/<session>')
