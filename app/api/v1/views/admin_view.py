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



