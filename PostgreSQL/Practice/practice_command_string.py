from db_connect import ConnectPsql
from psycopg2._psycopg import cursor
from pprint import pprint

connect_psql = ConnectPsql.create_con()

with connect_psql.cursor() as cur:

    cur: cursor
    cur.execute(
        """
        select payment_id as "№ платежа",
               customer_id "№ покупалеля",
               amount as "Сума платежа"
        from payment;       
        """
    )
    pprint(cur.fetchall())
    pprint('__________________')
    cur.execute(
        """
        select
            concat('title: ' ,title , '; ' , 'description: ', description ),
            substring(title,1,strpos(title,' ')-1) as Name 
        from
            film;
        """
    )
    pprint(cur.fetchall())
