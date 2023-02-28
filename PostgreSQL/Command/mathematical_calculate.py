from db_connect import ConnectPsql
from psycopg2._psycopg import cursor
from pprint import pprint

con_psql = ConnectPsql.create_con()
"""Математические функции"""
with con_psql.cursor() as cur:
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