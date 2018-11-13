orders = []
users = []


class UserModel(object):
    """"Class to handle user models."""

    def __init__(self):
        self.orders = orders
        self.users = users

    def create_user(self, username, password, phone, email):
        """Method to create a user"""
        payload = {
            "user_id": len(self.orders) + 1,
            "username": username,
            "password": password,
            "phone": phone,
            "email": email
        }
        self.users.append(payload)

    def create_order(self, pickup_location, destination, weight, quote, status):
        """"Method to create a parcel order deliveries."""

        payload = {
            "order_id": len(self.orders) + 1,
            "user_id": len(self.users) + 1,
            "pickup_location": pickup_location,
            "destination": destination,
            "weight": weight,
            "quote": quote,
            "status": status
        }
        self.orders.append(payload)

    def cancel_order(self, parcelId):
        """"Method to cancel a parcel order delivery."""
        new_order = next((order for order in self.orders if order[
            "order_id"] == parcelId), None)
        new_order["status"] = "cancelled"
        return new_order
