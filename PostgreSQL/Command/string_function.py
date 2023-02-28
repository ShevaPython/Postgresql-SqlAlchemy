from db_connect import ConnectPsql
from psycopg2._psycopg import cursor
from pprint import pprint

""""
1)Обьединения колонок,конкатенация
concat(first_name,' ',last_name) 
first_name || ' ' || last_name

2)Узнать оличество символов
char_length(first_name || ' ' || last_name)

3)Удаления лишних пробелов
trim('     ' || first_name || '   ')  
trim(leading '     ' || first_name || '   ') - удаления пробелов в начале
TRAILING - удаления пробелов в конце
trim('er' from first_name) -удалить er в имени

4)Берем определенное количество символов в строке
substring(first_name,1,3) - строка,с какого символа,количество

5)Регистр
upper(first_name) верхний регистр
lower(first_name) нижний регистр

6)Номер позиции символа
strpose(email,'@') 
"""

connection_psql = ConnectPsql.create_con()

with connection_psql.cursor() as cur:
    cur: cursor
    cur.execute(

        """select first_name,
                  last_name,
                  concat(first_name,' ',last_name),
                  first_name || ' ' || last_name ,
                  char_length(first_name || ' ' || last_name),
                  trim('     ' || first_name || '   '),
                  substring(first_name,1,3) || '' || substring(last_name,1,3),
                  trim('pe' from first_name) ,
                  upper(first_name),
                  lower(first_name)
           from actor;"""
    )
    pprint(cur.fetchone())
    pprint("_____________________________________________")
    cur.execute(
        """select email,
                  strpos(email,'@'),
                  substring(email,1,strpos(email,'@')-1)
           from staff;
        """
    )

    pprint(cur.fetchall())

