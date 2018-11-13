from flask import Blueprint
from flask_restful import Api, Resource
from .views.admin_view import AllOrders, OneOrder, AllOrdersByUser, AllUsers, OneUser
from .views.user_view import CreateOrder, CancelOrder, CreateUser

version1_blueprint = Blueprint('apiv1', __name__)
api = Api(version1_blueprint)
api.add_resource(AllOrders, '/parcels')
api.add_resource(OneOrder, '/parcels/<int:parcelId>')
api.add_resource(AllOrdersByUser, '/users/<int:userId>/parcels')
api.add_resource(CreateOrder, '/parcels')
api.add_resource(CancelOrder, '/parcels/<int:parcelId>/cancel')
api.add_resource(AllUsers, '/users')
api.add_resource(OneUser, '/users/<int:userId>')
api.add_resource(CreateUser, '/users')
