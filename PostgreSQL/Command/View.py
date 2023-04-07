from db_connect import con
from psycopg2._psycopg import cursor
from pprint import pprint
from psycopg2 import Error

"""View - убирает дублирование кода
CREATE materialized view - создаст таблицу с которой можно читать
"""


con.autocommit = True

try:
    with con.cursor() as cur:
        """
        Будет выполнен не select запрос а создано представления!
        """

        cur: cursor
        cur.execute(
            '''
            CREATE materialized view film_amount_view  AS 
            SELECT 
                f.film_id,
                sum(p.amount)
            FROM 
                film f
                left join inventory i on f.film_id = i.film_id
                left join rental r on i.inventory_id = r.inventory_id
                left join payment p on r.rental_id = p.rental_id
            GROUP BY f.film_id;
            
            
            SELECT
                *
            FROM
                 film_amount_view ;''')

        pprint(cur.fetchall())

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if con:
        con.close()
        print("База даных закрыта")
