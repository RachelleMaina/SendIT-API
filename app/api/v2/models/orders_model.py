from app.db_config import db_init


class OrdersModel(object):
    """"Class to handle admin models."""

    def __init__(self):
        self.db = db_init()

    def serialize_order(self, all_orders):
        """"Method to create serialize parcel order rows to dict deliveries."""
        orders = []
        for i, order_from_db in enumerate(all_orders):
            order_id, user_id, pickup_location, destination, current_location, weight, price, status= order_from_db
            order = dict(order_id=order_id, user_id=user_id, pickup_location=pickup_location,
                         destination=destination, current_location=current_location, weight=weight, price=price, status=status)
            orders.append(order)

        return orders

    def create_order(self, user_id, pickup_location, destination, weight, price):
        """"Method to create a parcel order deliveries."""

        cur = self.db.cursor()
        query = """INSERT INTO orders(user_id, pickup_location, destination, weight, price)
         VALUES(%s, %s, %s, %s, %s)"""
        data = (user_id, pickup_location,
                destination, weight, price)
        cur.execute(query, data)
        self.db.commit()
        self.db.close()

    def get_all_orders(self):
        """"Method to fetch all parcel order deliveries."""

        self.db = db_init()
        cur = self.db.cursor()
        cur.execute(
            """SELECT order_id, user_id, pickup_location, destination, current_location, weight, price, status FROM orders""")
        all_orders= cur.fetchall()
        if cur.rowcount >= 1:
            resp = self.serialize_order(all_orders)
            return resp
        
        return None
        self.db.close()

        

    def get_one_order(self, parcelId):
        """"Method to fetch one parcel order delivery"""

        self.db = db_init()
        cur = self.db.cursor()
        cur.execute("""SELECT user_id, user_id, pickup_location, destination, weight, price, status, date_created  FROM orders WHERE order_id = %s""", (parcelId, ))
        all_orders= cur.fetchone()

        
        return cur.rowcount
        self.db.close()
        
        


    def change_status(self, status, parcelId):
        """"Method to change status of  a parcel order delivery."""

        cur = self.db.cursor()
        query = """UPDATE orders set status = %s where order_id = %s """
        data = (status, parcelId)
        cur.execute(query, data)
        self.db.commit()
        self.db.close()

    def get_all_orders_by_user(self, userId):
        """"Method to fetch all parcel order deliveries by a specific user."""

        self.db = db_init()
        cur = self.db.cursor()
        cur.execute("""SELECT order_id, user_id, pickup_location, destination, weight, price, status FROM orders WHERE user_id = %s""", (userId, ))
        all_orders= cur.fetchall()
        if cur.rowcount >= 1:
            resp = self.serialize_order(all_orders)
            return resp
        
        return None
        self.db.close()

    def change_location(self, current_location, parcelId):
        """"Method to change location of  a parcel order delivery."""

        cur = self.db.cursor()
        query = """UPDATE orders set current_location = %s where order_id = %s """
        data = (current_location, parcelId)
        cur.execute(query, data)
        self.db.commit()
        self.db.close()

       