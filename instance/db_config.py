import psycopg2
import os
from passlib.hash import pbkdf2_sha256 as sha256


url = os.getenv('DB_URL')


def connection(url):
    con = psycopg2.connect(url)
    return con


def db_init():
    con = connection(url)
    return con


def create_tables():

    con = connection(url)
    cur = con.cursor()
    queries = tables()

    for query in queries:
        cur.execute(query)
    con.commit()


def destroy_tables():
    con = connection(url)
    cur = con.cursor()
    orders = "DROP TABLE IF EXISTS orders CASCADE;"
    users = "DROP TABLE IF EXISTS users CASCADE;"
    queries = [orders, users]
    for query in queries:
        cur.execute(query)
    con.commit()



def tables():
    users = """CREATE TABLE IF NOT EXISTS users(
        user_id serial PRIMARY KEY NOT NULL,
        username varchar(50) UNIQUE NOT NULL,
        password varchar(200) NOT NULL,
        phone varchar(50) UNIQUE NOT NULL,
        email varchar(50) UNIQUE NOT NULL,
        role varchar(50) NOT NULL DEFAULT 'User',
        date_created timestamp with time zone DEFAULT ('now'::text)::date
    );"""

    orders = """CREATE TABLE IF NOT EXISTS orders(
        order_id serial PRIMARY KEY NOT NULL,
        user_id integer REFERENCES users(user_id) ON DELETE CASCADE,
        pickup_location varchar(50) NOT NULL,
        destination varchar(50) NOT NULL,
        current_location varchar(50) NOT NULL DEFAULT '',
        weight varchar(50)NOT NULL,
        price varchar(50)  NOT NULL,
        status varchar(50) NOT NULL DEFAULT 'Pending Delivery',
        date_created timestamp with time zone DEFAULT ('now'::text)::date
    ); """


    queries = (users, orders)
    return queries

def generate_hash(password):
        return sha256.hash(password)

def create_admin():
    """"Method to create admin account."""
   
    con = connection(url)
    cur = con.cursor()
    query = """INSERT INTO users( username, password, phone, email, role)
     VALUES(%s, %s, %s, %s, %s)"""
    password = generate_hash("maina")
    data = ("Maina", password, "254712123345", "maina@gmail.com", "Admin")
    cur.execute(query, data)
    con.commit()  
    con.close()

def create_user():
    """"Method to create admin account."""
   
    con = connection(url)
    cur = con.cursor()
    query = """INSERT INTO users( username, password, phone, email, role)
     VALUES(%s, %s, %s, %s, %s)"""
    password = generate_hash("mercy")
    data = ("Mercy", password, "254712123785", "mercy@gmail.com", "User")
    cur.execute(query, data)
    con.commit()  
    con.close()

def create_order():
    """"Method to create admin account."""
   
    con = connection(url)
    cur = con.cursor()
    
    query = """INSERT INTO orders(user_id, pickup_location, destination, weight, price)
     VALUES(%s, %s, %s, %s, %s)"""
    data = (1, "Limuru", "Narok", "20", "2000")
    cur.execute(query, data)
    con.commit()
    con.close()
    