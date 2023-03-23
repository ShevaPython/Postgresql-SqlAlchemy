from db_connect import con
from psycopg2._psycopg import cursor
from pprint import pprint

"""
union - получаем все уникальные елементы
union all -получаем все строки даже их дубликаты
except - выполняеться 1 запрос и исключаем все строки 2 запроса
intersect - получаем строки которые попадают и в 1 и в 2 запросе
"""

def union1():
    """Union - служить для обьединения двух отдельных запросов,самое главное чтобы
    поля select были одинакового типаи их количество,в результате обьединения выводяться уникальные значения"""
    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            '''
            select
                f.title
            from
                film  f
                join inventory i on f.film_id = i.film_id
                join rental r on i.inventory_id = r.inventory_id
                join payment p on r.rental_id = p.rental_id
            group by 
                f.title
            having
                sum(p.amount) >150              
            union            
            select 
                f.title
            from 
                film f
            where
                f.rental_rate > 4;                      
            '''
        )
        return cur.fetchall()


# pprint(union1())

def except_union():
    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            '''
            select
                f.title,
                f.rental_rate,
                f.rental_duration,
                f.rating
            from
                film  f
                join inventory i on f.film_id = i.film_id
                join rental r on i.inventory_id = r.inventory_id
                join payment p on r.rental_id = p.rental_id
            group by 
                1,2,3,4
            having
                sum(p.amount) >150              
            except           
            select 
                   f.title,
                f.rental_rate,
                f.rental_duration,
                f.rating
            from 
                film f
            where
                f.rating = 'G';                      
            '''
        )
        return cur.fetchall()


# pprint(except_union())

def intersect():
    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            '''
            select
                f.title,
                f.rental_rate,
                f.rental_duration,
                f.rating
            from
                film  f
                join inventory i on f.film_id = i.film_id
                join rental r on i.inventory_id = r.inventory_id
                join payment p on r.rental_id = p.rental_id
            group by 
                1,2,3,4
            having
                sum(p.amount) >150              
            intersect          
            select 
                   f.title,
                f.rental_rate,
                f.rental_duration,
                f.rating
            from 
                film f
            where
                f.rating = 'G';                      
            '''
        )
        return cur.fetchall()


pprint(intersect())