from db_connect import con
from psycopg2._psycopg import cursor
from pprint import pprint


"""Математические функции"""
with con.cursor() as cur:
    cur: cursor
    cur.execute(
        """
        select 
            amount,
            amount - 5,
            amount + 5,
            amount * 5,
            amount / 5,
            amount ^ 5,
            div(amount,2),
            round(amount/2,1),
            floor(amount/2),
            ceil(amount/2)
        from     
            public.payment;
        """
    )

    pprint(cur.fetchone())