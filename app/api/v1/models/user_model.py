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

 
