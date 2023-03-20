from db_connect import con
from psycopg2._psycopg import cursor



def dz():
    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            """
            select
             a.first_name || ',' || a.last_name,
             count(fa.film_id) as film_cnt
            from
                actor a
                join film_actor fa on a.actor_id = fa.actor_id
            group by   a.first_name || ',' || a.last_name,a.actor_id
            order by 2 desc ,1 asc 
            limit 5
            offset 5 ;    
            """
        )

        return cur.fetchall()


print(dz())