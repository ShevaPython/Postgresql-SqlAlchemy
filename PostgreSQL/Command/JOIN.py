from db_connect import con
from psycopg2._psycopg import cursor
from pprint import pprint

"""
Join -соединения таблиц

using(film_id) - если сравнения двух таблиц по 1 полю
"""


def inner_join():
    with con.cursor() as cur:
        """Обьединения двух таблиц и создание новой результируещей с данными с 1 и 2
        таблицы!Inner join возвращает соединения 2 таблиц данные которых есть и в 1 и во 2 одновремменно"""

        cur: cursor

        # cur.execute(
        #     """
        #     select
        #        film.title,
        #        language.name
        #     from
        #         film
        #         inner join language
        #             on film.language_id = language.language_id;
        #     """
        # )
        # return cur.fetchall()
        cur.execute(
            """
            select 
               film.title,
               language.name 
            from 
                film 
                inner join language 
                    using (language_id);    
            """
        )
        return cur.fetchall()


# pprint(inner_join())


def left_join():
    with con.cursor() as cur:
        """Обьединения двух таблиц и создание новой результируещей с данными с 1 и 2
        таблицы!left join возвращает соединения 2 таблиц данные которых есть и в 1 и во 2 
        даже если данных во второй таблице нету вернеть результат null"""

        cur: cursor

        cur.execute(
            """
                        select 
                *
            from
                film f
            left  join inventory i
                    using(film_id)
            where
                i.inventory_id is null ;  
        
            """
        )
        return cur.fetchall()


# pprint(left_join())

def right_join():
    with con.cursor() as cur:
        """Обьединения двух таблиц и создание новой результируещей с данными с 1 и 2
        таблицы!Right join возвращает соединения 2 таблиц данные которых есть и в 1 и во 2 
        даже если данных в 1 таблице нету вернеть результат null"""

        cur: cursor

        cur.execute(
            """
                        select 
                *
            from
                film f
            right join 
                inventory i
                    using(film_id)
 ;  

            """
        )
        return cur.fetchall()

# pprint(right_join())

def cross_join():
    with con.cursor() as cur:
        """Обьединения двух таблиц и создание новой результируещей с данными с 1 и 2
        таблицы!Cross join возвращает всевозможные пары с 1 и 2 таблицы"""

        cur: cursor

        cur.execute(
            """
            select 
                f.title,
                a.first_name || ' ' || a.last_name as actor_name
            from
                film f
            cross join 
                actor a;
                    
 ;  

            """
        )
        return cur.fetchall()

pprint(cross_join()[:100])