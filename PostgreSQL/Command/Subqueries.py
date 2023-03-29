from db_connect import con
from psycopg2._psycopg import cursor
from pprint import pprint

"""
Subqueries.py - подзапрос,это когда у нас в нутри запроса другой запрос.
"""

def exists():
    """
    Для удаления всех неиспользуемых данных!При использовании exists  мы можем использовать подзапрос
    который возращает любое количество строк с любым количеством колонок и мы
    можем в этом подзапросе ссылаться на поня внешнего подзапроса!Когда мы ссылаемся на поля внешнего запросса
    называються связанными или коллерируещими!
    """
    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            '''
             select
                *
             from
                address a
             where 
                    not exists(
                    select 1
                    from 
                        customer c
                    where 
                        c.address_id= a.address_id 
                    );                      
            '''
        )
        return cur.fetchall()


# pprint(exists())


def function_in():
    """
    В подзапросе с функцией in должен возвращать только 1 колонку и выражения слева будет
    сравниваться из значением колонки каждой строки!Если запрос не ссылаеться не на 1 как в этом
    случае не на 1 из таблиц внешнего запроса!Не колерируещий подзапрос,несвязаный!
    """
    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            '''


            select 
                f.title,
                c.name as category_name
            from
                film f 
                join film_category fc on f.film_id = fc.film_id
                join category c on c.category_id = fc.category_id 
                
                where 
                    c.category_id in(            
                    select
                        fc.category_id
                
                    from
                        film_category fc
                    group by 
                        1
                    having 
                        count(*) >70)   
                        
                ;                         
            '''
        )
        return cur.fetchall()


pprint(function_in())