from db_connect import con
from psycopg2._psycopg import cursor
from pprint import pprint

"""
Distinct
Выбор всех уникальных значений,дубликаты удаляються

"""


def distinct1():
    with con.cursor() as cur:
        """Выбор найбольшего уникального значения"""
        cur: cursor

        cur.execute(
            """
            select distinct
                max(rental_rate)
            from 
                film;    
            """
        )
        return cur.fetchall()


# pprint(distinct1())


def distinct2():
    with con.cursor() as cur:
        """Выбор найбольшего уникального значения"""
        cur: cursor

        cur.execute(
            """
            select distinct
                first_name,
                last_name
            from 
                actor
            order by 1   ;    
            """
        )
        return cur.fetchall()

# pprint(distinct2())

def distinct3():
    with con.cursor() as cur:
        """Взять по 1 уникальному значению!"""
        cur: cursor

        cur.execute(
            """
            select distinct on (rental_rate)
                title
            from 
                film
            order by rental_rate,title   ;    
            """
        )
        return cur.fetchall()


pprint(distinct3())
