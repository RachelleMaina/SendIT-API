from flask import Blueprint
from flask_restful import Api, Resource
from .views.users_view import Register, Login
from .views.orders_view import CreateOrder, ChangeDestination, AllOrdersinApplication

version2_blueprint = Blueprint('apiv2', __name__)
api = Api(version2_blueprint)
api.add_resource(Register, '/auth/signup')
api.add_resource(Login, '/auth/login')
api.add_resource(CreateOrder, '/parcels')
api.add_resource(AllOrdersinApplication, '/parcels')
api.add_resource(ChangeDestination, '/parcels/<parcelId>/destination')



