from db_connect import con
from psycopg2._psycopg import cursor
from pprint import pprint

"""Group_by

Групировки
"""
def group_by():
    with con.cursor() as cur:
        """Сортировка по группам и вывод 1 уникального значенния для него,
        и популярные функции"""

        cur.execute(
            """
            select 
               rating,
               count(*) films_count,
                sum(length) total_length,
                max(length) as max_length,
                min(length) as min_length,
                round( avg(length),2) as avg_length,
                bool_and(length < 200),
                string_agg(title,'; ') 
            from 
                film
            group by 
                rating    
;    
            """
        )
        return cur.fetchall()


# pprint(group_by())

def group_by1():
    with con.cursor() as cur:
        """
        Групировка сразу по нескольким значениям"""

        cur.execute(
            """
            select 
               rating,
               rental_rate,
               substring(title,1,1)
            from 
                film
            group by 
                rating,
                rental_rate,
                substring(title,1,1)
            order by 1,2       
;    
            """
        )
        return cur.fetchall()


# pprint(group_by1())


def group_by2():
    with con.cursor() as cur:
        """
        Групировка сразу по нескольким значениям"""

        cur.execute(
            """
            select 
               count(*),
               f.title
            from 
                inventory
                join film f on f.film_id = inventory.film_id
            group by f.title
                
     
;    
            """
        )
        return cur.fetchall()


# pprint(group_by2())


def group_by3():
    with con.cursor() as cur:
        """
        Групировка сразу по нескольким значениям и связыванием таблиц плюс условиие"""

        cur.execute(
            """
            select 
                 f.title,
                 count(*) as payment_count
               
            from film f 
                join inventory
                    using (film_id)
                join rental
                    using (inventory_id)
                join payment
                    using (rental_id)      
            
            where 
                f.rental_rate > 2
            
            group by f.title
            having  count(*) > 10 
            order by payment_count

;    
            """
        )
        return cur.fetchall()


pprint(group_by3())


def group_by4():
    with con.cursor() as cur:
        """
        Групировка c условием"""

        cur.execute(
            """
            select 
            concat(a.first_name,' ',a.last_name) as actor_name,
            count(*) as film_count,
            count(distinct fc.category_id) as category_count

            from actor a
                join film_actor fa
                    using (actor_id)
                join film_category fc
                    using(film_id)
            group by actor_name

;    
            """
        )
        return cur.fetchall()


pprint(group_by4())