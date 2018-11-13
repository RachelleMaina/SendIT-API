orders = []
users = []


class AdminModel(object):
    """"Class to handle admin models."""

    def __init__(self):
        self.orders = orders
        self.users = users

    def get_all_orders(self):
        """"Method to fetch all parcel order deliveries."""
        return self.orders

    def get_one_order(self, parcelId):
        """"Method to fetch one parcel order delivery"""

        new_order = next((order for order in self.orders
                          if order["order_id"] == parcelId), None)
        return new_order

   