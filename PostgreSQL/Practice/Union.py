from db_connect import con
from psycopg2._psycopg import cursor
from pprint import pprint

def dz1():
    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            '''
            select
                f.title
            from
                film  f
            where
                f.rating = 'G'                            
            union all          
            select 
                f.title
            from 
                film f
                join film_actor fa on f.film_id = fa.film_id
                join actor a on a.actor_id = fa.actor_id
            where
                a.last_name = 'Grant'
                ;                      
            '''
        )
        return cur.fetchall()


# pprint(dz1())

def dz2():
    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            '''
            select
                f.title
            from
                film  f
            where
                f.rating = 'G'                            
            intersect          
            select 
                f.title
            from 
                film f
                join film_actor fa on f.film_id = fa.film_id
                join actor a on a.actor_id = fa.actor_id
            where
                a.last_name = 'Grant'
                ;                      
            '''
        )
        return cur.fetchall()

#
# pprint(dz2())

def dz3():
    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            '''
            select 
                f.title
            from 
                film f
                join film_actor fa on f.film_id = fa.film_id
                join actor a on a.actor_id = fa.actor_id
            where
                a.last_name = 'Grant'
                
            except    
            select
                f.title
            from
                film  f
            where
                f.rating = 'G'                            
       

                ;                      
            '''
        )
        return cur.fetchall()


pprint(dz3())