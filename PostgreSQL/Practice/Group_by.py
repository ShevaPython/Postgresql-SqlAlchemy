from db_connect import con
from psycopg2._psycopg import cursor
from pprint import pprint


def group_by_hw1():
    with con.cursor() as cur:

        cur.execute(
            """
            select 
              f.title,
              sum(p.amount) as amount
            from 
                film f
                join inventory i on f.film_id = i.film_id
                join rental r on i.inventory_id = r.inventory_id
                join payment p on r.rental_id = p.rental_id
            group by f.title
            order by 2 desc 
;    
            """
        )
        return cur.fetchall()


# pprint(group_by_hw1())

def group_by_hw2():
    with con.cursor() as cur:

        cur.execute(
            """
            select 
                concat(a.first_name,' ',a.last_name) as actor_name,
                count(fa.film_id)
                   
            from 
                actor a
                 join film_actor fa on a.actor_id = fa.actor_id
            group by actor_name
            having count(fa.film_id) >20
;           
            """
        )
        return cur.fetchall()


# pprint(group_by_hw2())


def group_by_hw3():
    with con.cursor() as cur:
        cur.execute(
            """
            select 
                count(*)

            from 
                film
            where film.length > 120
;           
            """
        )
        return cur.fetchall()


# pprint(group_by_hw3())

def group_by_hw4():
    with con.cursor() as cur:
        cur.execute(
            """
            select 
                c.name,
                count(f.film_id)

            from 
                category c
            left join film_category fc on c.category_id = fc.category_id
            left join film f on fc.film_id = f.film_id and f.length > 180
            group by c.name
;           
            """
        )
        return cur.fetchall()


pprint(group_by_hw4())