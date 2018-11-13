from flask import request, make_response, jsonify, abort
from flask_restful import Resource
from ..models.user_model import UserModel


class CreateOrder(Resource, UserModel):
    """"Class to handle  create parcel order deliveries."""

    def post(self):
        """"Http method to create parcel order deliveries."""
        data = request.get_json() or {}

        if 'pickup_location' not in data:
            abort(make_response(jsonify(message="Missing pickup_location"), 400))
        if 'destination' not in data:
            abort(make_response(jsonify(message="Missing destination"), 400))
        if 'weight' not in data:
            abort(make_response(jsonify(message="weight"), 400))
        if 'quote' not in data:
            abort(make_response(jsonify(message="quote"), 400))
        if 'status' not in data:
            abort(make_response(jsonify(message="status"), 400))
        if len(data) == 0:
            abort(make_response(jsonify(message="Fields are empty"), 400))
        if len(data) >5:
            abort(make_response(jsonify(message="Unwanted field given"), 400))

        order = self.create_order(
            pickup_location=data["pickup_location"],
            destination=data["destination"],
            weight=data["weight"],
            quote=data["quote"],
            status=data["status"]

        )

        return make_response(jsonify({
            "status": "Created",
        }), 201)


class CancelOrder(Resource, UserModel):
    """"Class to handle cancel parcel order deliveries."""

    def put(self, parcelId):
        """"Http method to cancel a parcel order delivery."""
        order = self.cancel_order(parcelId)
        if order is not None:
            return make_response(jsonify(
                {
                    "Status": "Order Cancelled",

                }), 200)

        return make_response(jsonify(
            {
                "status": "Not Found"
            }), 404)


class CreateUser(Resource, UserModel):
    """Class to handle user  methods"""

    def post(self):
        """Method to create a user"""
        data = request.get_json() or {}

        if 'username' not in data:
            abort(make_response(jsonify(message="username"), 400))
        if 'password' not in data:
            abort(make_response(jsonify(message="password"), 400))
        if 'phone' not in data:
            abort(make_response(jsonify(message="email"), 400))
        if 'email' not in data:
            abort(make_response(jsonify(message="email"), 400))
        if len(data) == 0:
            abort(make_response(jsonify(message="Fields are empty"), 400))
        if len(data) >4:
            abort(make_response(jsonify(message="Unwanted Field given"), 400))

        data = request.get_json() or {}
        user = self.create_user(
            username=data["username"],
            password=data["password"],
            phone=data["phone"],
            email=data["email"]
        )
        return make_response(jsonify({
            "status": "Created",
        }), 201)
