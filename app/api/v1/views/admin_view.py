from flask import request, make_response, jsonify
from flask_restful import Resource
from ..models.admin_model import AdminModel


class AllOrders(Resource, AdminModel):
    """"Class to handle all parcel order deliveries views."""

    def get(self):
        """"Http method to get all parcel order deliveries."""
        order = self.get_all_orders()
        if order is not None:
            return make_response(jsonify(
                {
                    "status": "Ok",
                    "Order": order
                }), 200)

        return make_response(jsonify(
            {
                "status": "Not Found"
            }), 404)


class OneOrder(Resource, AdminModel):
    """"Class to handle one parcel order delivery views."""

    def get(self, parcelId):
        """"Http method to get one parcel order delivery."""

        order = self.get_one_order(parcelId)
        if order is not None:
            return make_response(jsonify(
                {
                    "status": "Ok",
                    "Order": order
                }), 200)

        return make_response(jsonify(
            {
                "status": "Not Found"
            }), 404)


class AllOrdersByUser(Resource, AdminModel):
    """"Class to handle all parcel order deliveries by a specific user views."""

    def get(self, userId):
        """"Http method to get all parcel order deliveries by a specific user."""

        order = self.get_all_orders_by_user(userId)
        if order is not None:
            return make_response(jsonify({
                "status": "Ok",
                "Order": order
            }), 200)

        return make_response(jsonify({
            "status": "Not Found"
        }), 404)


class AllUsers(Resource, AdminModel):
    """Class to handle all users."""

    def get(self):
        """Method to return all users"""
        user = self.get_all_users()
        if user is not None:
            return make_response(jsonify({
                "status": "Ok",
                "User": user
            }), 200)
        return make_response(jsonify({
            "status": "Not Found"
            }), 404)



class OneUser(Resource, AdminModel):
    """Class handle a single user."""

    def get(self, userId):
        """method to fetch a single user."""
        user = self.get_one_user(userId)
        if user is not None:
            return make_response(jsonify({
                "status": "Ok",
                "User": user
            }), 200)

        return make_response(jsonify({
            "status": "Not Found"
        }), 404)
