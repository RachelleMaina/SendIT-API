import psycopg2
from passlib.hash import pbkdf2_sha256 as sha256
from instance.db_config import db_init


class UsersModel(object):
    """"Class to handle admin models."""

    def __init__(self):
        self.db = db_init()


    def serialize_user(self, user_from_db):
        users = []
        for i, all_users in enumerate(user_from_db):
            user_id, username, phone, email, role, date_created = all_users
            user = dict(user_id=user_id, username=username,
                         phone=phone, email=email, role=role, date_created=date_created)
            users.append(user)

        return users

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)


    def login(self, user_username, user_password):
        """Method to login."""


        cur = self.db.cursor()
        cur.execute(
            """SELECT user_id, username, password, phone, email, role
            FROM users WHERE username = %s """, (user_username, ))
        user_from_db = cur.fetchone()

        if cur.rowcount == 1: 
          
            user_id, username, password, phone, email, role  = user_from_db
            resp = dict(user_id=user_id, username=username, password=password, phone=phone, email=email, role=role)
            
            if self.verify_hash(user_password, resp["password"]):            
                return resp
        return None



    def register(self, username, password, phone, email):
        """"Method to create user account."""
       
        cur = self.db.cursor()
        query = """INSERT INTO users( username, password, phone, email)
         VALUES(%s, %s, %s, %s) RETURNING username, password, phone, email;"""
        
        data = (username, password, phone, email)
        cur.execute(query, data)
        self.db.commit()
       

    def user_by_id(self, user_id):
        """Method to fetch one user."""

        cur = self.db.cursor()
        cur.execute(
            """SELECT user_id, username, password, phone, email, role
            FROM users WHERE user_id = %s""", (user_id, ))
        
        user_from_db = cur.fetchone()
        if cur.rowcount == 1: 
            user_id, username, password, phone, email, role  = user_from_db
            resp = dict(user_id=user_id, username=username, password=password, phone=phone, email=email, role=role)
                                
            return resp
        return None

    def all_users(self):
        """Method to fetch one user."""

        cur = self.db.cursor()
        cur.execute(
            """SELECT user_id, username, phone, email, role, date_created 
            FROM users""")
        
        user_from_db = cur.fetchall()
        if cur.rowcount >= 1: 
            resp = self.serialize_user(user_from_db)                     
            return resp
        return None

 

    



