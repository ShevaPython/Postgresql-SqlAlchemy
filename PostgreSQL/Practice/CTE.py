from db_connect import con
from psycopg2._psycopg import cursor
from pprint import pprint



def dzcte():

    with con.cursor() as cur:

        cur: cursor
        cur.execute(
            '''
            with amount_actor as (select
                                        film_id,
                                        count(*) as cnt
                                  from 
                                        film_actor fa
                                  group by 
                                        1     
                                                   
                                        ),
            film_amount as (select 
                                    i.film_id,
                                    sum(p.amount) as amount
                            from inventory i
                                 join rental r on i.inventory_id = r.inventory_id
                                 join payment p on r.rental_id = p.rental_id 
                                 group by 1     
                                )    
                                
            select
            f.title,
            amount_actor.cnt,
            film_amount.amount
            from
                film f
                left join amount_actor using (film_id)
                left join film_amount using (film_id);
                                                          
                                  
            '''
        )
        return cur.fetchall()


pprint(dzcte())
