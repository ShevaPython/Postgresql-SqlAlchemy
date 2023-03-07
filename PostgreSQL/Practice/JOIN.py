from db_connect import con
from psycopg2._psycopg import cursor
from pprint import pprint


def hw1():
    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            """
            select
                a.first_name,
                a.last_name
            from
                actor a 
                inner join film_actor fa on a.actor_id = fa.actor_id
                inner join film f on fa.film_id = f.film_id  
  
            where f.title = 'Chamber Italian'
            """
        )
        return cur.fetchall()


# pprint(hw1()[:10])

def hw2():
    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            """
            select
            f.title
            
            from
                film f
                inner join  film_category fc on f.film_id = fc.film_id
                inner join category c on fc.category_id = c.category_id
                where c.name='Comedy'

 
            """
        )
        return cur.fetchall()


# pprint(hw2())

def hw3():
    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            """
            select
            f.title,
            c.name

            from
                film f
                inner join  film_category fc on f.film_id = fc.film_id
                inner join category c on fc.category_id = c.category_id


            """
        )
        return cur.fetchall()


# pprint(hw3()[:10])


def hw4():
    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            """
            select
            f.title,
            c.name,
            fc.film_id is not null

            from
                film f
                cross join
                category c
                left join film_category fc on f.film_id = fc.film_id and c.category_id = fc.category_id


            """
        )
        return cur.fetchall()


# pprint(hw4()[:100])

def hw5():
    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            """
            select
            f.title
            
            from
                film f
                left join inventory i on f.film_id = i.film_id
            where i.film_id is null   
            
                


            """
        )
        return cur.fetchall()


pprint(hw5()[:100])

