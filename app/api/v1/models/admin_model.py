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

    