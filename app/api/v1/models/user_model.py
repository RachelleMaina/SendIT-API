orders = []
users = []


class UserModel(object):
    """"Class to handle user models."""

    def __init__(self):
        self.orders = orders
        self.users = users



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

 
