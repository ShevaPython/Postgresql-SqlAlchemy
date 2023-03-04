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


pprint(inner_join())


def inner_join():
    with con.cursor() as cur:
        """Обьединения двух таблиц и создание новой результируещей с данными с 1 и 2
        таблицы!left join возвращает соединения 2 таблиц данные которых есть и в 1 и во 2 
        даже если данных во второй таблице нету вернеть результат null"""

        cur: cursor

        cur.execute(
            """
            select 
               film.title,
               language.name 
            from 
                film 
                inner join language 
                    on film.language_id = language.language_id;    
            """
        )
        return cur.fetchall()
