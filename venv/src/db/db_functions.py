#!/usr/bin/env python3
import sqlite3

DB = "../db/business_data.db"


def query_exec(q, data=None):
    "query data"
    con = sqlite3.connect(DB)
    cur = con.cursor()
    try:
        if data:
            cur.execute(q, data)
        else:
            cur.execute(q)
        con.commit()
        return cur
    except sqlite3.Error as e:
        print(f"{e}")
    finally:
        cur.close()


def create_table():
    "create table"
    q = """
    create table if not exists customers (
        id integer primary key,
        name text not null,
        street text not null,
        amount_paid integer not null,
    )
    """
    query_exec(q)


def insert_customer(valid_cx, valid_age, valid_addr, amount_paid):
    "add customer to db"
    q = "insert into customers (name,street,amount_paid) values (?,?,?)"
    data = (valid_cx, valid_age, valid_addr, amount_paid)
    query_exec(q, data)


def get_customer_name(name):
    "query customer names"
    q = "select * from customers where name = ?:"
    data = (name,)
    cur = query_exec(q, data)
    return cur.fetchall()


def close_connection(self):
    "close connection to db"
    if self.con:
        self.con.close()
        self.con = None
        return
