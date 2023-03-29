from db_connect import con
from psycopg2._psycopg import cursor
from pprint import pprint

"""
CTE - общие таблияные выражения!
"""

def cte1():

    with con.cursor() as cur:
        """CTE  нужен для раздиления больших запросов на части,для удобочитаемости"""
        cur: cursor
        cur.execute(
            '''
            with filter_category as (select 
                                        fc.category_id,
                                        c.name as categoty_name,
                                        count(*) as count_cnt
                                     from
                                            film_category fc
                                            join category c on c.category_id = fc.category_id
                                     group by 1,2
                                     having count(*) > 70       
                                        )  
            select 
                f.title, 
                filter_category.categoty_name,
                filter_category.count_cnt
            from 
                film f 
                join film_category fc on f.film_id= fc.film_id
                join filter_category on filter_category.category_id = fc.category_id                                     
            '''
        )
        return cur.fetchall()


pprint(cte1())
