import re
from flask import request, make_response, jsonify, abort
from flask_restful import Resource
from ..models.order_model import OrderModel


class CreateOrder(Resource, OrderModel):
    """"Class to handle  create parcel order deliveries."""

    def post(self):
        """"Http method to create parcel order deliveries."""

        data = request.get_json() or {}
        if 'user_id' not in data:
            abort(make_response(jsonify(message="Data Supplied Missing user_id"), 400))
        if 'pickup_location' not in data:
            abort(make_response(jsonify(message="Data Supplied Missing pickup_location"), 400))
        if 'destination' not in data:
            abort(make_response(jsonify(message="Data Supplied Missing destination"), 400))
        if 'weight' not in data:
            abort(make_response(jsonify(message="Data Supplied Missing weight"), 400))
        if 'price' not in data:
            abort(make_response(jsonify(message="Data Supplied Missing price"), 400))   
        if len(data) == 0:
            abort(make_response(jsonify(message="Fields are empty"), 400))
        if len(data) > 5:
            abort(make_response(jsonify(message="Data Supplied has Unwanted Fields"), 400))
        
        user_id = str(data["user_id"])
        pickup_location = str(data["pickup_location"])
        destination = str(data["destination"])
        weight = str(data["weight"])
        price = str(data["price"])

        if user_id.isdigit() == False:
            abort(make_response(jsonify(message="user_id should be a number"), 400))
        if weight.isdigit() == False:
            abort(make_response(jsonify(message="weight should be a number"), 400))    
        if price.isdigit() == False:
            abort(make_response(jsonify(message="price should be a number"), 400)) 
        if destination.isalpha() == False:
            abort(make_response(jsonify(message="destination should have letters only"), 400))    
        if pickup_location.isalpha() == False:
            abort(make_response(jsonify(message="pickup_location  should have letters only"), 400)) 
        if self.get_one_user(int(user_id)) is None:
            abort(make_response(jsonify(message="User with id " + str(user_id) + " does not exist"), 400)) 


        order = self.create_order(
            user_id=int(user_id),
            pickup_location=pickup_location,
            destination=destination,
            weight=int(weight),
            price=int(price)

        )

        return make_response(jsonify({
            "Message": "Order Created", "Order": order
        }), 201)


class AllOrders(Resource, OrderModel):
    """"Class to handle all parcel order deliveries views."""

    def get(self):
        """"Http method to get all parcel order deliveries."""
        order = self.get_all_orders()
        if order is not None:
            return make_response(jsonify(
                {
                    "Message": "All Orders",
                    "Order": order
                }), 200)

        return make_response(jsonify(
            {
                "Message": "No Orders Found"
            }), 404)


class OneOrder(Resource, OrderModel):
    """"Class to handle one parcel order delivery views."""

    def get(self, parcelId):
        """"Http method to get one parcel order delivery."""
        parcelId = str(parcelId)
        if parcelId.isdigit():
            order = self.get_one_order(parcelId)

            message = "Order with id " + str(parcelId)
            err = "Order with given id does not exist"
            if order is not None:
                return make_response(jsonify(
                    {
                        "Message": message,
                        "Order": order
                    }), 200)

            return make_response(jsonify(
                {
                    "Message": err
                }), 404)
        return make_response(jsonify(
            {
                "Message": "parcelId given is not a number"
            }), 404)


class AllOrdersByUser(Resource, OrderModel):
    """"Class to handle all parcel order deliveries by a specific user views."""

    def get(self, userId):
        """"Http method to get all parcel order deliveries by a specific user."""
        userId = str(userId)
        if userId.isdigit():
            order = self.get_all_orders_by_user(userId)
            message = "All orders by User with id " + str(userId)
            err = "User with given id does not exist"
            if order is not None:
                return make_response(jsonify({
                    "Message": message,
                    "Order": order
                }), 200)

            return make_response(jsonify({
                "Message": str(err)
            }), 404)
        return make_response(jsonify(
            {
                "Message": "userId given is not a number"
            }), 404)


class AllUsers(Resource, OrderModel):
    """Class to handle all users."""

    def get(self):
        """Method to return all users"""
        user = self.get_all_users()
        if user is not None:
            return make_response(jsonify({
                "Message": "All users",
                "User": user
            }), 200)



class Signin(Resource, OrderModel):
    """Class handle a single user."""

    def get(self, userId):
        """method to fetch a single user."""
        userId = str(userId)
        if userId.isdigit():
            user = self.get_one_user(userId)
            err = "User with given id  does not exist"
            if user is not None:
                return make_response(jsonify({
                    "Message": "User Signed in",
                    "User": user
                }), 200)

            return make_response(jsonify({
                "Message": err
            }), 404)
        return make_response(jsonify(
            {
                "Message": "userId given is not a number"
            }), 404)


class CancelOrder(Resource, OrderModel):
    """"Class to handle cancel parcel order deliveries."""

    def put(self, parcelId):
        """"Http method to cancel a parcel order delivery."""
        if self.get_one_order(int(parcelId)) is None:
            abort(make_response(jsonify({
                "Message": "Order with given id does not exist"

                }), 400)) 

        order = self.cancel_order(parcelId)
        message = "Order with id " + str(parcelId) + " Cancelled"
        if order is not None:
                return make_response(jsonify(
                    {
                        "Message": message,
                        "Order": order
                    }), 200)

        return make_response(jsonify(
                {
                    "Message": "Order with given id does not exist"
                }), 404)
   

class Register(Resource, OrderModel):
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
        if len(data) > 4:
            abort(make_response(jsonify(message="Unwanted Field given"), 400))
        username = str(data["username"])
        password=str(data["password"])
        phone = str(data["phone"])
        email = str(data["email"])  
        if phone.isdigit() == False and len(phone)!=10:
            abort(make_response(jsonify(message="phone should be a number with 10 digits"), 400)) 
        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
            abort(make_response(jsonify(message="Email given is not valid"), 400)) 


        data = request.get_json() or {}
        user = self.create_user(
            username=username,
            password=password,
            phone=phone,
            email=email
        )
        return make_response(jsonify({
            "Message": "User Signed up", "User": user
        }), 201)
