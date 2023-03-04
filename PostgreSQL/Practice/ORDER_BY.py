from db_connect import con
from psycopg2._psycopg import cursor
from pprint import pprint


def hw1():
    with con.cursor() as cur:
        cur: cursor

        cur.execute(
            """
            select
                title,
                length as "len"
            from
                film
            order by len   ;    
            """
        )
        return cur.fetchall()[:10]


# pprint(hw1())

def hw2():
    with con.cursor() as cur:
        cur: cursor

        cur.execute(
            """
            select
                rental_duration,
                length,
                title
            from
                film
            order by 2/1 desc  ;    
            """
        )
        return cur.fetchall()[:10]


# pprint(hw2())


def hw3():
    with con.cursor() as cur:
        cur: cursor

        cur.execute(
            """
            select
                *
            from
                film
            order by rating asc ,length desc ;    
            """
        )
        return cur.fetchall()[:10]


pprint(hw3())