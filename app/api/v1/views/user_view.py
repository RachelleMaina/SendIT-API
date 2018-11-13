from flask import request, make_response, jsonify, abort
from flask_restful import Resource
from ..models.user_model import UserModel




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
