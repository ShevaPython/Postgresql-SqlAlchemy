from db_connect import con
from psycopg2._psycopg import cursor
from pprint import pprint

"""
over() - означает что эта функция оконая и идет описанния окна
over(partition by ) - аналог group by 
partition by - если не указывать этот параметр over() то найдеться минимальное значения
Окоными функциями могут быть все агрегатные функции
window - создаем окно,которое можем применять с функцией over что бы убрать дублирования кода

По мимо агрегатных функций есть ранжируищие функции,которые по каждой строке дают какой либо номер
 row_number() over (partition by f.rating) - нумерация по рейтингам
 row_number() over (partition by f.rating order by f.length) - сгрупировать, пронумеровать,отсортеровать
                                                               по продолжительности!
dense_rank()-у строк который порядок сортировки одинаковый и продолжительность дает один и тотже номер 
rank() - у строк который порядок сортировки одинаковый и продолжительность дает один и тотже номер как если бы 
                использовали row_number()

lag(f.length,1) over (partition by f.rating order by f.length) - получение преведушего значения(1 - какое значения,
                                                                                                2-на какое смещения)
lead(f.length,1) over (partition by f.rating order by f.length)-получение следущего значения 
f.length - lag(f.length,1) over( partition by f.rating order by f.length) - разница между сегодня и вчера                                                                                                                                                                              
"""


def window_function():
    with con.cursor() as cur:
        """min(f.length) over(partition by f.rating) идет сортировка и групировка по рейтингу
        и ставиться значения для каждого поля с оприделеным рейтингом"""

        cur: cursor
        cur.execute(
            '''
            select
                f.title,
                f.rating,
                f.length,
                min(f.length) over(partition by f.rating),
                max(f.length) over(partition by f.rating), 
                avg(f.length) over(partition by f.rating), 
                sum(f.length) over(partition by f.rating), 
                count(f.length) over(partition by f.rating)  
            from
                film f
            order by f.rating,f.length   ;    
            '''

        )
        return cur.fetchall()


# pprint(window_function())

def window():
    with con.cursor() as cur:
        """
        window w as (partition by f.rating) - можем указать окно,которое применяем к ower
        """

        cur: cursor
        cur.execute(
            '''
            select
                f.title,
                f.rating,
                f.length,
                min(f.length) over w,
                max(f.length) over w, 
                avg(f.length) over w , 
                sum(f.length) over w, 
                count(f.length) over w  
            from
                film f
            window w as (partition by f.rating)   
            order by f.rating,f.length   ;    
            '''

        )
        return cur.fetchall()


# pprint(window())

def row_number():
    with con.cursor() as cur:
        """
        row_number() over (partition by f.rating) - пронумеровувывает поочередно строки с определеным рейтингом
        """

        cur: cursor
        cur.execute(
            '''
            select
                f.title,
                f.rating,
                f.length,
                row_number() over (partition by f.rating),
                row_number() over (partition by f.rating order by f.length)
 
            from
                film f  ;    
            '''

        )
        return cur.fetchall()


# pprint(row_number())


def rank():
    with con.cursor() as cur:
        """
        dense_rank()-у строк который порядок сортировки одинаковый и продолжительность дает один и тотже номер
        rank() - у строк который порядок сортировки одинаковый и продолжительность дает один и тотже номер как если бы 
                использовали row_number()
        """

        cur: cursor
        cur.execute(
            '''
            select
                f.title,
                f.rating,
                f.length,
                rank() over(partition by f.rating order by f.length),
                dense_rank() over(partition by f.rating order by f.length)

            from
                film f  ;    
            '''

        )
        return cur.fetchall()


# pprint(rank())


def lag():
    with con.cursor() as cur:
        """
        lag(f.length,1) over (partition by f.rating order by f.length) - получение преведушего значения фильма
        lead(f.length,1) over (partition by f.rating order by f.length)-получение следущего значения фильма
        f.length - lag(f.length,1) over( partition by f.rating order by f.length) - разница между сегодня и вчера
        """

        cur: cursor
        cur.execute(
            '''
            select
                f.title,
                f.rating,
                f.length,
                lag(f.length,1) over (partition by f.rating order by f.length),
                lead(f.length,1) over (partition by f.rating order by f.length),
                f.length - lag(f.length,1) over( partition by f.rating order by f.length)


            from
                film f  ;    
            '''

        )
        return cur.fetchall()


pprint(lag())
