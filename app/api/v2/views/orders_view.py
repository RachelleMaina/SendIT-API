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
