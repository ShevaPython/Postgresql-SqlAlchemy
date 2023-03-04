from db_connect import con
from psycopg2._psycopg import cursor
from pprint import pprint


def hw1():
    with con.cursor() as cur:
        """Выбор найбольшего уникального значения"""
        cur: cursor

        cur.execute(
            """
            select distinct
                rental_duration
            from 
                film  ;    
            """
        )
        return cur.fetchall()


# pprint(hw1())

def hw2():
    with con.cursor() as cur:
        """Выбор найбольшего уникального значения"""
        cur: cursor

        cur.execute(
            """
            select distinct
                substring(first_name,1,3)
            from 
                actor  ;    
            """
        )
        return cur.fetchall()


# pprint(hw2())

def hw3():
    with con.cursor() as cur:
        """Выбор найбольшего уникального значения"""
        cur: cursor

        cur.execute(
            """
            select distinct on (customer_id)
                payment_id,
                customer_id,
                amount,
                payment_date
            from 
                payment
            order by customer_id,payment_date desc     ;    
            """
        )
        return cur.fetchall()


pprint(hw3())
