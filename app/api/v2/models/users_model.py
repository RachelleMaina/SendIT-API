import psycopg2
from passlib.hash import pbkdf2_sha256 as sha256
from app.db_config import db_init


class UsersModel(object):
    """"Class to handle admin models."""

    def __init__(self):
        self.db = db_init()


    def serialize_user(self, user_from_db):

        user_id, username, password, phone, email, role, date_created = user_from_db
        user = dict(user_id=user_id, username=username, password=password,
                     phone=phone, email=email, role=role, date_created=date_created)

        return user

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)


    def login(self, username, password):
        """Method to login."""


        cur = self.db.cursor()
        cur.execute(
            """SELECT user_id, username, password, phone, email, role, date_created
            FROM users WHERE username = %s """, (username, ))
        user_from_db = cur.fetchone()
        if cur.rowcount == 1: 
            resp = self.serialize_user(user_from_db)
            if self.verify_hash(password, resp["password"]) is True:  
            
                return resp



    def register(self, username, password, phone, email):
        """"Method to create user account."""
       
        cur = self.db.cursor()
        query = """INSERT INTO users( username, password, phone, email)
         VALUES(%s, %s, %s, %s)"""
        
        data = (username, password, phone, email)
        cur.execute(query, data)
        self.db.commit()
        return "Signed up successifully"
    
        self.db.close()

    def user_by_id(self, userId):
        """Method to fetch one user."""

        cur = self.db.cursor()
        cur.execute(
            """SELECT user_id, username, password, phone, email, role, date_created 
            FROM users WHERE user_id = %s""", (userId, ))
        
        user_from_db = cur.fetchone()
        if cur.rowcount == 1: 
            resp = self.serialize_user(user_from_db)                     
            return resp
        return None

    def user_by_username(self, username):
        """Method to fetch one user."""

        cur = self.db.cursor()
        cur.execute(
            """SELECT user_id, username, password, phone, email, role, date_created 
            FROM users WHERE username = %s""", (username, ))
        
        user_from_db = cur.fetchone()
        if cur.rowcount == 1: 
            resp = self.serialize_user(user_from_db)                     
            return resp
        return None

 

    



