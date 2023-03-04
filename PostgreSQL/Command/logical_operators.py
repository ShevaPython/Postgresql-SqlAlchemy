from db_connect import ConnectPsql
from psycopg2._psycopg import cursor
from pprint import pprint

"""
WHERE-ограничения выбора!

1) = -равно,
2) >,< больше меньше
3) <=,>= меньше или равно,больше или равно

4)BETWEEN - диапозон с такого по такое
5)AND - или
6)OR - или 1 или 2
7)LIKE - where title like '%Airport%' - строка слева удовлетворяет шаблону справа -регистр важен!
  NOT LIKE - не соответствует шаблону
8)%-любое количество символов,  _ -один символ! 
9) IS NULL -если ячейки пусты
   IS NOT NULL - не пустые ячейки
10)  <>  или != -не равен!   
"""

con = ConnectPsql.create_con()

with con.cursor() as con_cur:
    con_cur: cursor
    con_cur.execute(
        """
        select 
            * 
        from 
            film
        where
            rental_rate = 4.99  ;
        """
    )

    pprint([i for i in con_cur][:10])
    pprint('______________________________')
    con_cur.execute(
        """
        select 
            * 
        from
            rental
        where 
            rental_date between '2005-05-26' and '2005-05-28';
        """
    )

    pprint([i for i in con_cur][:10])
    pprint('______________________________')
    con_cur.execute(
        """
        select 
            *
        from 
            film
         where title like '%Airport%'     
        """
    )
    pprint([i for i in con_cur][:10])
    pprint('______________________________')