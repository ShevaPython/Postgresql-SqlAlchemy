from pprint import pprint
from db_connect import ConnectPsql


con = ConnectPsql.create_con()

with con.cursor() as cur:
    # Взять все колонки из таблицы актер!
    cur.execute(
        """select 
                *

           from
                actor;"""


    )
    pprint(F"Server version : {cur.fetchall()}")