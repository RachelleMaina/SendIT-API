import psycopg2
import os


url = "dbname = 'sendit' host = 'localhost' port = '5432'\
     user = 'rachel' password = 'rachel100'"

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
        username varchar(50)  NOT NULL,
        password varchar(50) NOT NULL,
        phone varchar(50) NOT NULL,
        email varchar(50) NOT NULL,
        role varchar(50) NOT NULL DEFAULT 'User',
        date_created timestamp with time zone DEFAULT ('now'::text)::date
    );"""

    orders = """CREATE TABLE IF NOT EXISTS orders(
        order_id serial PRIMARY KEY NOT NULL,
        user_id integer REFERENCES users(user_id) ON DELETE CASCADE,
        pickup_location varchar(50) NOT NULL,
        destination varchar(50) NOT NULL,
        weight varchar(50)NOT NULL,
        price varchar(50)  NOT NULL,
        status varchar(50) NOT NULL DEFAULT 'Pending Delivery',
        date_created timestamp with time zone DEFAULT ('now'::text)::date
    ); """

    queries = (users, orders)
    return queries
