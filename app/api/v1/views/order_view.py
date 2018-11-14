from flask import request, make_response, jsonify, abort
from flask_restful import Resource
from ..models.order_model import OrderModel


class CreateOrder(Resource, OrderModel):
    """"Class to handle  create parcel order deliveries."""

    def post(self):
        """"Http method to create parcel order deliveries."""
        data = request.get_json() or {}

        if 'pickup_location' not in data:
            abort(make_response(jsonify(message="Missing pickup_location"), 400))
        if 'destination' not in data:
            abort(make_response(jsonify(message="Missing destination"), 400))
        if 'weight' not in data:
            abort(make_response(jsonify(message="Missing weight"), 400))
        if 'quote' not in data:
            abort(make_response(jsonify(message="Missing quote"), 400))
        if 'status' not in data:
            abort(make_response(jsonify(message="Missing status"), 400))
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
            "status": "Order Created", "Order": order
        }), 201)

class AllOrders(Resource, OrderModel):
    """"Class to handle all parcel order deliveries views."""

    def get(self):
        """"Http method to get all parcel order deliveries."""
        order = self.get_all_orders()
        if order is not None:
            return make_response(jsonify(
                {
                    "status": "All Orders",
                    "Order": order
                }), 200)

        return make_response(jsonify(
            {
                "status": "No Orders Found"
            }), 404)


class OneOrder(Resource, OrderModel):
    """"Class to handle one parcel order delivery views."""

    def get(self, parcelId):
        """"Http method to get one parcel order delivery."""

        order = self.get_one_order(parcelId)
        status = "Order with id " +  str(parcelId)
        err = "Order with id " + str(parcelId) + " Not Found"
        if order is not None:
            return make_response(jsonify(
                {
                    "status": status,
                    "Order": order
                }), 200)

        return make_response(jsonify(
            {
                "status": err
            }), 404)


class AllOrdersByUser(Resource, OrderModel):
    """"Class to handle all parcel order deliveries by a specific user views."""

    def get(self, userId):
        """"Http method to get all parcel order deliveries by a specific user."""

        order = self.get_all_orders_by_user(userId)
        status = "All orders by User with id " + str(userId)
        err = "User with id " + str(userId) +" Not Found"
        if order is not None:
            return make_response(jsonify({
                "status": status,
                "Order": order
            }), 200)

        return make_response(jsonify({
            "status": str(err)
        }), 404)


class AllUsers(Resource, OrderModel):
    """Class to handle all users."""

    def get(self):
        """Method to return all users"""
        user = self.get_all_users()
        if user is not None:
            return make_response(jsonify({
                "status": "All users",
                "User": user
            }), 200)
        return make_response(jsonify({
            "status": "Not Found"
            }), 404)



class OneUser(Resource, OrderModel):
    """Class handle a single user."""

    def get(self, userId):
        """method to fetch a single user."""
        user = self.get_one_user(userId)
        status = "User with id " + str(userId)
        err = "User with id " + str(userId) + " Not Found"
        if user is not None:
            return make_response(jsonify({
                "status": status,
                "User": user
            }), 200)

        return make_response(jsonify({
            "status": err
        }), 404)



class CancelOrder(Resource, OrderModel):
    """"Class to handle cancel parcel order deliveries."""

    def put(self, parcelId):
        """"Http method to cancel a parcel order delivery."""
        order = self.cancel_order(parcelId)
        status = "Order with id " + str(parcelId)+ " Cancelled"
        err = "Order with id " + str(parcelId) + " Not Found"
        if order is not None:
            return make_response(jsonify(
                {
                    "Status": status, 
                    "Order": order
                }), 200)

        return make_response(jsonify(
            {
                "Status": err
            }), 404)


class CreateUser(Resource, OrderModel):
    """Class to handle user  methods"""

    def post(self):
        """Method to create a user"""
        data = request.get_json() or {}

        if 'username' not in data:
            abort(make_response(jsonify(message="Missing username"), 400))
        if 'password' not in data:
            abort(make_response(jsonify(message="Missing password"), 400))
        if 'phone' not in data:
            abort(make_response(jsonify(message="Missing Phone"), 400))
        if 'email' not in data:
            abort(make_response(jsonify(message="Missing email"), 400))
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
            "status": "User Created", "User": user
        }), 201)
