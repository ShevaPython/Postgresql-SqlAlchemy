from db_connect import con
from psycopg2._psycopg import cursor


"""
limit- сколько нужно взять записей из бд
offset - сколько нужно пропустить
order by - обезателен,что бы порядок был одинаковым
limit all - взять все строки
"""


def lim_offs1():
    """Берем первые 50 строк limit"""
    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            """
            select
             title
            from
                film
            order by 1
            limit 50  ;    
            """
        )

        return cur.fetchall()


print(lim_offs1())


def lim_offs2():
    """Берем следущие  50 строк limit,offset"""
    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            """
            select
             title
            from
                film
            order by 1
            limit 50
            offset 50 ;    
            """
        )

        return cur.fetchall()


print(lim_offs2())