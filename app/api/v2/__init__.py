from flask import Blueprint
from flask_restful import Api, Resource
from .views.users_view import Register, Login
from .views.orders_view import CreateOrder, AllOrdersinApplication, ChangeStatus,ChangeLocation, ChangeDestination, AllOrdersByUser


version2_blueprint = Blueprint('apiv2', __name__)
api = Api(version2_blueprint)
api.add_resource(Register, '/auth/signup')
api.add_resource(Login, '/auth/login')
api.add_resource(CreateOrder, '/parcels')
api.add_resource(AllOrdersinApplication, '/parcels')
api.add_resource(ChangeStatus, '/parcels/<parcelId>/status')
api.add_resource(ChangeLocation, '/parcels/<parcelId>/presentLocation')
api.add_resource(AllOrdersByUser, '/user/parcels')
api.add_resource(ChangeDestination, '/parcels/<parcelId>/destination')






