import re
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from flask import request, make_response, jsonify, abort
from flask_restful import Resource, reqparse
from ..models.users_model import UsersModel


class Login(Resource, UsersModel):
    """Class handle a single user."""

    def post(self):
        """method to fetch a single user."""
        parser = reqparse.RequestParser()
        parser.add_argument(
            'username', help='username cannot be blank', required=True)
        parser.add_argument(
            'password', help='password cannot be blank', required=True)
        data = parser.parse_args()
        username = data["username"]
        password = data["password"]

        try:
            user = self.login(username, password)
            access_token = create_access_token(identity = username)
            refresh_token = create_refresh_token(identity = password)
            return make_response(jsonify({
                "Message": "Signed in as " + user["role"],
                'access_token': access_token,
                'refresh_token': refresh_token
            }), 200)

        except:
            return make_response(jsonify({
                "Message": "Invalid Password or username"
            }), 200)


class Register(Resource, UsersModel):
    """Class to handle user  methods"""

    def post(self):
        """Method to create a user"""
        parser = reqparse.RequestParser()
        parser.add_argument(
            'username', help='username cannot be blank', required=True)
        parser.add_argument(
            'password', help='password cannot be blank', required=True)
        parser.add_argument(
            'email', help='email cannot be blank', required=True)
        parser.add_argument(
            'phone', help='phone cannot be blank', required=True)
        data = parser.parse_args()
        username = str(data["username"])
        password = self.generate_hash(data['password'])
        phone = str(data["phone"])
        email = str(data["email"])


        try:
            user = self.register(
                username=username, password=password, phone=phone, email=email)
            return make_response(jsonify({
                "Message": "Signup successiful"
            }), 201)
        except:
            return make_response(jsonify({
                    "Message": "username, password or email  already exists"
                    
                }), 200)




class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        user = get_jwt_identity()
        access_token = create_access_token(identity = user)
        return {'access_token': access_token}
