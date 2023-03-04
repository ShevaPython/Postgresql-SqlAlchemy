from db_connect import con
from psycopg2._psycopg import cursor
from pprint import pprint


"""
Сортировка по возростанию или убыванию!

ORDER BY

1) ask - сортировка по возростанию
2) desk - сортировка по убыванию
3) desk null last - null в конце
4)desk null first - null в начале
"""

with con.cursor() as cur:
    cur: cursor
    cur.execute(
        """
        select
            first_name
        from
            actor
        order by first_name asc ;      
        """
    )
    pprint(cur.fetchall()[:10])
