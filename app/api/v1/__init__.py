from flask import Blueprint
from flask_restful import Api, Resource
from .views.order_view import AllOrders, OneOrder, AllOrdersByUser, AllUsers, Signin, CreateOrder, CancelOrder, Register

version1_blueprint = Blueprint('apiv1', __name__)
api = Api(version1_blueprint)
api.add_resource(AllOrders, '/parcels')
api.add_resource(OneOrder, '/parcels/<parcelId>')
api.add_resource(AllOrdersByUser, '/users/<userId>/parcels')
api.add_resource(CreateOrder, '/parcels')
api.add_resource(CancelOrder, '/parcels/<parcelId>/cancel')
api.add_resource(AllUsers, '/users')
api.add_resource(Signin, '/users/<userId>')
api.add_resource(Register, '/users')

