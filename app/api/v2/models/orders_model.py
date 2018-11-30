from instance.db_config import db_init


class OrdersModel(object):
    """"Class to handle admin models."""

    def __init__(self):
        self.db = db_init()

    def serialize_order(self, all_orders):
        """"Method to create serialize parcel order rows to dict deliveries."""
        orders = []
        for i, order_from_db in enumerate(all_orders):
            order_id, user_id, pickup_location, destination, current_location, weight, price, status = order_from_db
            order = dict(order_id=order_id, user_id=user_id, pickup_location=pickup_location,
                         destination=destination, current_location=current_location, weight=weight, price=price, status=status)
            orders.append(order)

        return orders

    def create_order(self, user_id, pickup_location, destination, weight, price):
        """"Method to create a parcel order deliveries."""

        cur = self.db.cursor()
        query = """INSERT INTO orders(user_id, pickup_location, destination, current_location, weight, price)
         VALUES(%s, %s, %s, %s, %s, %s) RETURNING  pickup_location, destination, weight, price """
        data = (user_id, pickup_location,
                destination, pickup_location, weight, price)
        cur.execute(query, data)
        self.db.commit()


    def get_all_orders(self):
        """"Method to fetch all parcel order deliveries."""

        self.db = db_init()
        cur = self.db.cursor()
        cur.execute(
            """SELECT order_id, user_id, pickup_location, destination, 
            current_location, weight, price, status FROM orders""")
        all_orders = cur.fetchall()
        if cur.rowcount >= 1:
            resp = self.serialize_order(all_orders)
            return resp

        return None
       

    def get_one_order(self, parcelId):
        """"Method to fetch one parcel order delivery"""

        self.db = db_init()
        cur = self.db.cursor()
        cur.execute("""SELECT order_id, user_id, pickup_location, current_location, 
            destination, weight, price, status 
            FROM orders WHERE order_id = %s""", (parcelId, ))
        order_from_db = cur.fetchone()
        if cur.rowcount == 1:
            order_id, user_id, pickup_location, destination, current_location, weight, price, status = order_from_db
            order = dict(order_id=order_id, user_id=user_id, pickup_location=pickup_location,
                             destination=destination, current_location=current_location, weight=weight, price=price, status=status)
                
            return order
        return None



        

    def change_status(self, status, parcelId):
        """"Method to change status of  a parcel order delivery."""

        cur = self.db.cursor()
        query = """UPDATE orders set status = %s where order_id = %s  RETURNING status"""
        data = (status, parcelId)
        cur.execute(query, data)
        self.db.commit()
        order_from_db= str(cur.fetchone()[0]) 
        status = order_from_db
        order = dict(status=status)
            
        return order
        

    def get_all_orders_by_user(self, userId):
        """"Method to fetch all parcel order deliveries by a specific user."""

        self.db = db_init()
        cur = self.db.cursor()
        cur.execute("""SELECT order_id, user_id, pickup_location, destination,
         current_location, weight, price, status FROM orders WHERE user_id = %s""", (userId, ))
        all_orders = cur.fetchall()
        if cur.rowcount >= 1:
            resp = self.serialize_order(all_orders)
            return resp

        return None
       

    def change_location(self, current_location, parcelId):
        """"Method to change location of  a parcel order delivery."""

        cur = self.db.cursor()
        query = """UPDATE orders set current_location = %s where order_id = %s RETURNING current_location"""
        data = (current_location, parcelId)
        cur.execute(query, data)
        self.db.commit()
        order_from_db= str(cur.fetchone()[0]) 
        current_location= order_from_db
        order = dict(current_location=current_location)
            
        return order
        

    def change_destination(self, user_id, destination, parcelId):
        """"Method to change status of  a parcel order delivery."""

        cur = self.db.cursor()
        query = """UPDATE orders set destination = %s where user_id = %s and order_id = %s  RETURNING destination"""
        data = (destination, user_id, parcelId)
        cur.execute(query, data)
        self.db.commit()
        order_from_db= str(cur.fetchone()[0]) 
        if cur.rowcount == 1:
            destination= order_from_db
            order = dict(destination=destination)
                
            return order
        return None
            
       
        
