import re
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, get_jwt_identity, get_raw_jwt)
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

            access_token = create_access_token(identity = user)
            return make_response(jsonify({
                "Message": "Signed in as " + user["role"],
                'access_token': access_token
            }), 200)

        except:
            return make_response(jsonify({
                "Message": "Invalid Password or username"
            }), 404)




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
        stripped_username= username.strip()
        stripped_password= password.strip()
        stripped_phone= phone.strip()
        stripped_email= email.strip()

        if not stripped_username or not stripped_password or not stripped_phone or not stripped_email:
            abort(make_response(
                jsonify(message="password, email, phone and email fields cannot be empty"), 400))

        if not re.match("^[0-9]*$", phone) or len(phone) != 12:
            abort(make_response(
                jsonify(message="phone number should have 12 digits and of the format 254*********"), 400))

        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
            abort(make_response(jsonify(message="Email given is not valid"), 400))


        if not re.match("^[a-zA-Z _-]*$", username):
            abort(make_response(
                jsonify(message="username should have letters, spaces, _ and - only"), 400))


        try:
            user = self.register(
                username=username, password=password, phone=phone, email=email)
            return make_response(jsonify({
                "Message": "Signup successiful"
            }), 201)
        except:
            return make_response(jsonify({
                    "Message": "username, password or email  already exists"
                    
                }), 400)





