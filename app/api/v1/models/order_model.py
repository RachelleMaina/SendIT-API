
class OrderModel(object):
    """"Class to handle admin models."""
    orders = []
    users = []


    def get_all_orders(self):
        """"Method to fetch all parcel order deliveries."""
        return OrderModel.orders

    def get_one_order(self, parcelId):
        """"Method to fetch one parcel order delivery"""

        new_order = next((order for order in OrderModel.orders
                          if order["order_id"] == parcelId), None)
        return new_order

    def get_all_orders_by_user(self, userId):
        """"Method to fetch all parcel order deliveries by a specific user."""
        new_order = [order for order in OrderModel.orders if order[
            "user_id"] == userId]
        if len(new_order) == 0:
            return None
        return new_order

    def get_all_users(self):
        """Method to fetch all users."""
        return OrderModel.users

    def get_one_user(self, userId):
        """Method to fetch one user."""
        new_user = next((user for user in OrderModel.users if user[
            "user_id"] == userId), None)
        return new_user


    def create_user(self, username, password, phone, email):
        """Method to create a user"""
        payload = {
            "user_id": len(OrderModel.users) + 1,
            "username": username,
            "password": password,
            "phone": phone,
            "email": email
        }
        OrderModel.users.append(payload)
        return payload

    def create_order(self, pickup_location, destination, weight, quote, status):
        """"Method to create a parcel order deliveries."""

        payload = {
            "order_id": len(OrderModel.orders) + 1,
            "user_id": len(OrderModel.users) + 1,
            "pickup_location": pickup_location,
            "destination": destination,
            "weight": weight,
            "quote": quote,
            "status": status
        }
        OrderModel.orders.append(payload)
        return payload

    def cancel_order(self, parcelId):
        """"Method to cancel a parcel order delivery."""
        new_order = next((order for order in OrderModel.orders if order[
            "order_id"] == parcelId), None)
        new_order["status"] = "Cancelled"
        return new_order

 
