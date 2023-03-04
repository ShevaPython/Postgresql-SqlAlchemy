from db_connect import ConnectPsql
from psycopg2._psycopg import cursor
from pprint import pprint

con = ConnectPsql.create_con()


def hw():
    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            """
            select
                *
            from
                payment
            where amount > 7 and payment_date between '2007-03-01' and '2007-03-31';     
            """
        )
        return cur.fetchall()[:10]


# pprint(hw())

def hw2():
    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            """
            select 
                *
            from
                payment
             where amount > 7 or amount between 3.3 and 5.5;    
            """
        )
        return cur.fetchall()[:10]


# pprint(hw2())

def hw3():
    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            """
            select 
                *
            from
                payment
             where not (amount > 7) and not (amount between 3.3 and 5.5);    
            """
        )
        return cur.fetchall()[:10]


# pprint(hw3())
def hw4():
    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            """
            select 
                *
            from
                payment
             where  payment_id % 10 =1;    
            """
        )
        return cur.fetchall()[:10]


# pprint(hw4())

def hw5():
    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            """
            select 
                *
            from
                actor
             where  first_name like 'R%';    
            """
        )
        return cur.fetchall()[:10]


# pprint(hw5())


def hw6():
    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            """
            select 
                *
            from
                actor
             where  actor.last_name  not like '%a%';    
            """
        )
        return cur.fetchall()[:10]


# pprint(hw6())

def hw7():
    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            """
            select 
                title
            from
                film
             where  film.length in (87,116,184);    
            """
        )
        return cur.fetchall()[:10]


pprint(hw7())

