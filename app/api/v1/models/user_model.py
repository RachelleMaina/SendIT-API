orders = [{"order_id": 101, "user_id": 1, "pickup_location": "Nairobi",
          "destination": "Kisumu", "weight": 20, "quote": 2000, "status": "in transit"}]
users = [{"user_id": 201, "username": "Rachel", "password": "root",
         "phone": 712345123, "email": "rachel@gmail.com"}]


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

 
