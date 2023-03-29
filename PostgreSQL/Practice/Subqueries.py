from db_connect import con
from psycopg2._psycopg import cursor
from pprint import pprint



def dz1():

    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            '''
             select
                l.name
             from
                language l
             where 
                     not exists(
                    select 1
                    from 
                        film f 
                    where 
                        f.language_id = l.language_id 
                    );                      
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
                film f
            where f.film_id in (
                                  select 
                                        film_actor.film_id
                                  from 
                                       film_actor
                                       join actor a on a.actor_id = film_actor.actor_id
                                   where a.last_name like 'Chase%'  )  ;                      
            '''
        )
        return cur.fetchall()


# pprint(dz2())


def dz3():

    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            '''
             select
                film.title,
                (select
                    language.name 
                 from
                    language
                  where film.language_id=language.language_id )
             from
                film                          
            '''
        )
        return cur.fetchall()


pprint(dz3())