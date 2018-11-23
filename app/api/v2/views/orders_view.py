import re
from flask_jwt_extended import (create_access_token,
                                jwt_required, get_jwt_identity, get_raw_jwt, jwt_required)
from flask_mail import Message
from flask import request, make_response, jsonify, abort
from flask_restful import Resource, reqparse
from ..models.orders_model import OrdersModel
from ..models.users_model import UsersModel
from .email import Emails


class CreateOrder(Resource, OrdersModel):
    """"Class to handle  create parcel order deliveries."""
    @jwt_required
    def post(self):
        """"Http method to create parcel order deliveries."""
        users = get_jwt_identity()
        user_id = users["user_id"]

        if users["role"] == "User":
            parser = reqparse.RequestParser()
            parser.add_argument(
                'pickup_location', help='pickup_location cannot be blank', required=True)
            parser.add_argument(
                'destination', help='destination cannot be blank', required=True)
            parser.add_argument(
                'weight', help='weight cannot be blank', required=True)

            data = parser.parse_args()
            pickup_location = str(data["pickup_location"])
            destination = str(data["destination"])
            weight = str(data["weight"])
            price = 1000
            stripped_destination = destination.strip()
            stripped_pickup_location = pickup_location.strip()

            if weight.isdigit() is False:
                abort(make_response(
                    jsonify(message="weight should be a number"), 400))

            if not stripped_pickup_location:
                abort(make_response(
                    jsonify(message="pickup_location cannot be empty"), 400))
            if not stripped_destination:
                abort(make_response(
                    jsonify(message="destination cannot be empty"), 400))

            if not re.match("^[a-zA-Z _-]*$", destination):
                abort(make_response(
                    jsonify(message="destination should have letters, spaces, _ and - only"), 400))

            if not re.match("^[a-zA-Z _-]*$", pickup_location):
                abort(make_response(jsonify(
                    message="pickup_location should have letters, spaces, _ and - only"), 400))

            order = self.create_order(user_id=int(user_id), pickup_location=pickup_location,
                                      destination=destination, weight=int(weight), price=int(price))

            return make_response(jsonify({
                "Message": "Parcel Order Created Successifully"
                
            }), 201)


class AllOrdersinApplication(Resource, OrdersModel):
    """"Class to handle all parcel order deliveries views."""
    @jwt_required
    def get(self):
        """"Http method to get all parcel order deliveries."""
        users = get_jwt_identity()
        if users["role"] == "Admin":

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
                "Message": "Operation not allowed for this user"
            }), 404)


class ChangeStatus(Resource, OrdersModel):
    """"Class to handle cancel parcel order deliveries."""
    @jwt_required
    def put(self, parcelId):
        """"Http method to cancel a parcel order delivery."""

        users = get_jwt_identity()
        username = users["username"]
        if users["role"] == "Admin":
            status_message = ["In Transit", "Delivered", "Cancelled"]
            parser = reqparse.RequestParser()
            parser.add_argument(
                'status', help='status cannot be blank', required=True)
            data = parser.parse_args()
            status = data["status"]
            if status not in status_message:
                return make_response(jsonify(
                    {
                        "Message": "Status should be: In Transit, Delivered or Cancelled"
                    }), 404)

            parcelId = str(parcelId)
            if parcelId.isdigit() == False:
                abort(make_response(
                    jsonify(message="parcelId should be a number"), 400))

            if self.get_one_order(int(parcelId)) is None:
                abort(make_response(jsonify({
                    "Message": "Order with given id does not exist"

                }), 400))

            
            
            try:
                order = self.change_status(status, parcelId)
                one_order = self.get_one_order(parcelId)
                user_id = one_order["user_id"]
                one_user = UsersModel
                user_by_id = one_user.user_by_id(self, user_id)
                email = user_by_id["email"]
                user_email = Emails()
                user_email.change_status(email, order, user_by_id)
                return make_response(jsonify(
                    {
                        "Message": "Status of Order with id " + str(parcelId) + " Changed"

                    }), 200)
            except:
                return make_response(jsonify({
                    "Message": "A problem occured while trying to change parcel status. Please check the information given and try again"
                }), 400)
        return make_response(jsonify(
            {
                "Message": "Operation not allowed for this user"
            }), 404)


class AllOrdersByUser(Resource, OrdersModel):
    """"Class to handle all parcel order deliveries by a specific user views."""
    @jwt_required
    def get(self):
        """"Http method to get all parcel order deliveries by a specific user."""
        users = get_jwt_identity()
        username = users["username"]
        userId = users["user_id"]

        order = self.get_all_orders_by_user(userId)
        if order is not None:
            return make_response(jsonify({
                "Message": "All orders by User with id " + str(userId),
                "Data": order
            }), 200)

        return make_response(jsonify({
            "Message": "No parcel orders found"
        }), 404)


class ChangeLocation(Resource, OrdersModel):
    """"Class to  change location of  parcel order deliveries."""
    @jwt_required
    def put(self, parcelId):
        """"Http method to cancel a parcel order delivery."""

        users = get_jwt_identity()
        username = users["username"]
        if users["role"] == "Admin":
            parser = reqparse.RequestParser()
            parser.add_argument(
                'current_location', help='current_location cannot be blank', required=True)
            data = parser.parse_args()
            current_location = data["current_location"]
            parcelId = str(parcelId)
            if parcelId.isdigit() == False:
                abort(make_response(
                    jsonify(message="parcelId should be a number"), 400))

            if self.get_one_order(int(parcelId)) is None:
                abort(make_response(jsonify({
                    "Message": "Order with given id does not exist"

                }), 400))
            


            try:
                order = self.change_location(current_location, parcelId)
                one_order = self.get_one_order(parcelId)
                user_id = one_order["user_id"]
                one_user = UsersModel
                user_by_id = one_user.user_by_id(self, user_id)
                email = user_by_id["email"]
                user_email = Emails()
                user_email.change_location(email, order, user_by_id)
                return make_response(jsonify({
                    "Message": "Present Location of Order with id " + str(parcelId) + " Changed"

                }), 200)
            except:
                return make_response(jsonify({
                    "Message": "A problem occured while trying to change parcel location. Please check the information given and try again"
                }), 400)

        return make_response(jsonify(
            {
                "Message": "Operation not allowed for this user"
            }), 400)


class ChangeDestination(Resource, OrdersModel):
    """"Class to handle cancel parcel order deliveries."""
    @jwt_required
    def put(self, parcelId):
        """"Http method to cancel a parcel order delivery."""
        users = get_jwt_identity()
        username = users["username"]
        user_id = users["user_id"]

        if users["role"] == "User":
            parser = reqparse.RequestParser()
            parser.add_argument(
                'destination', help='destination cannot be blank', required=True)
            data = parser.parse_args()
            destination = data["destination"]
            parcelId = str(parcelId)
            if parcelId.isdigit() == False:
                abort(make_response(
                    jsonify(message="parcelId should be a number"), 400))

            if self.get_one_order(int(parcelId)) is None:
                abort(make_response(jsonify({
                    "Message": "Parcel Order with given id does not exist"

                }), 400))

  
            try:
                order = self.change_destination(user_id, destination, parcelId)
                one_order = self.get_one_order(parcelId)
                email = users["email"]
                user_email = Emails()
                user_email.change_destination(email, order, users)
                return make_response(jsonify({
                    "Message": "Destination of Order with id " + str(parcelId) + " Changed"

                }), 200)
            except:
                return make_response(jsonify({
                    "Message": "A problem occured while trying to change parcel destination. Please check the information given and try again"
                }), 400)
        return make_response(jsonify(
            {
                "Message": "Operation not allowed for this user"
            }), 400)
