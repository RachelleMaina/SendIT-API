import re
from flask_jwt_extended import (create_access_token,
                                jwt_required, get_jwt_identity, get_raw_jwt, jwt_required)
from flask import request, make_response, jsonify, abort
from flask_restful import Resource, reqparse
from ..models.orders_model import OrdersModel
from ..models.users_model import UsersModel


class CreateOrder(Resource, OrdersModel):
    """"Class to handle  create parcel order deliveries."""

    def post(self):
        """"Http method to create parcel order deliveries."""
        parser = reqparse.RequestParser()
        parser.add_argument(
            'user_id', help='user_id cannot be blank', required=True)
        parser.add_argument(
            'pickup_location', help='pickup_location cannot be blank', required=True)
        parser.add_argument(
            'destination', help='destination cannot be blank', required=True)
        parser.add_argument(
            'weight', help='weight cannot be blank', required=True)

        data = parser.parse_args()
        user_id = str(data["user_id"])
        pickup_location = str(data["pickup_location"])
        destination = str(data["destination"])
        weight = str(data["weight"])
        price = 1000

        if user_id.isdigit() is False or  weight.isdigit() is False:
            abort(make_response(
                jsonify(message="user_id and weight should be a number"), 400))


        user = UsersModel()

        if user.user_by_id(int(user_id)) is None:
            abort(make_response(jsonify(message="User with id " +
                                        str(user_id) + " does not exist"), 400))


        order = self.create_order(user_id=int(user_id), pickup_location=pickup_location,
                                  destination=destination, weight=int(weight), price=int(price))

        return make_response(jsonify({
            "Message": "Parcel Order Created"
        }), 201)

class AllOrdersinApplication(Resource, OrdersModel):
    """"Class to handle all parcel order deliveries views."""
    @jwt_required
    def get(self):
        """"Http method to get all parcel order deliveries."""
        username = get_jwt_identity()
        user = UsersModel()
        user_role=user.user_by_username(username)
        if user_role["role"] == "Admin":

            order = self.get_all_orders()
            if order is not None:
                return make_response(jsonify(
                    {
                        "Message": "All Parcel Orders",
                        "Order": order
                    }), 200)

            return make_response(jsonify(
                {
                    "Message": "No Orders Found"
                }), 404)
        return make_response(jsonify(
                {
                    "Message": "Method not allowed for this user"
                }), 404)


class ChangeStatus(Resource, OrdersModel):
    """"Class to handle cancel parcel order deliveries."""
    @jwt_required
    def put(self, parcelId):
        """"Http method to cancel a parcel order delivery."""
        username = get_jwt_identity()
        user = UsersModel()
        user_role=user.user_by_username(username)
        if user_role["role"] == "Admin":
            parser = reqparse.RequestParser()
            parser.add_argument(
                'status', help='status cannot be blank', required=True)
            data = parser.parse_args()
            status = data["status"]
            parcelId = str(parcelId)
            if parcelId.isdigit() == False:
                abort(make_response(jsonify(message="parcelId should be a number"), 400))

            if self.get_one_order(int(parcelId)) is None:
                abort(make_response(jsonify({
                    "Message": "Order with given id does not exist"

                }), 400))

            order = self.change_status(status, parcelId)
            
            return make_response(jsonify(
                    {
                        "Message": "Status of Order with id " + str(parcelId) + " Changed"
                        
                    }), 200)
        return make_response(jsonify(
                {
                    "Message": "Method not allowed for this user"
                }), 404)


class AllOrdersByUser(Resource, OrdersModel):
    """"Class to handle all parcel order deliveries by a specific user views."""
    @jwt_required
    def get(self):
        """"Http method to get all parcel order deliveries by a specific user."""
        username = get_jwt_identity()
        user = UsersModel()
        user_data=user.user_by_username(username)
        
        userId = user_data["user_id"]
        
        order = self.get_all_orders_by_user(userId)
        if order is not None:
            return make_response(jsonify({
                "Message": "All orders by User with id " + str(userId),
                "Order": order
            }), 200)

        return make_response(jsonify({
            "Message": "No parcel orders found"
        }), 404)
      
class ChangeLocation(Resource, OrdersModel):
    """"Class to  change location of  parcel order deliveries."""
    @jwt_required
    def put(self, parcelId):
        """"Http method to cancel a parcel order delivery."""
        username = get_jwt_identity()
        user = UsersModel()
        user_role=user.user_by_username(username)
        if user_role["role"] == "Admin":
            parser = reqparse.RequestParser()
            parser.add_argument(
                'current_location', help='current_location cannot be blank', required=True)
            data = parser.parse_args()
            current_location = data["current_location"]
            parcelId = str(parcelId)
            if parcelId.isdigit() == False:
                abort(make_response(jsonify(message="parcelId should be a number"), 400))

            if self.get_one_order(int(parcelId)) is None:
                abort(make_response(jsonify({
                    "Message": "Order with given id does not exist"

                }), 400))

            order = self.change_location(current_location, parcelId)
            
            return make_response(jsonify(
                    {
                        "Message": "Destination of Order with id " + str(parcelId) + " Changed"
                        
                    }), 200)
        return make_response(jsonify(
                {
                    "Message": "Method not allowed for this user"
                }), 404)
class ChangeDestination(Resource, OrdersModel):
    """"Class to handle cancel parcel order deliveries."""
    @jwt_required
    def put(self, parcelId):
        """"Http method to cancel a parcel order delivery."""
        username = get_jwt_identity()
        user = UsersModel()
        user_role = user.user_by_username(username)
        user_id = user_role["user_id"]
        
        if user_role["role"] == "User":
            parser = reqparse.RequestParser()
            parser.add_argument(
                'destination', help='destination cannot be blank', required=True)
            data = parser.parse_args()
            destination = data["destination"]
            parcelId = str(parcelId)
            if parcelId.isdigit() == False:
                abort(make_response(jsonify(message="parcelId should be a number"), 400))

            if self.order_by_id(int(parcelId)) is None:
                abort(make_response(jsonify({
                    "Message": "Parcel Order with given id does not exist"

                }), 400))

            order = self.change_destination(user_id, destination, parcelId)
            
            return make_response(jsonify(
                    {
                        "Message": "Destination of parcel order with id " + str(parcelId) + " changed successfully"
                        
                    }), 200)
        return make_response(jsonify(
                {
                    "Message": "Method not allowed for this user"
                }), 404)