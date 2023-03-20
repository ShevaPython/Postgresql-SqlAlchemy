from db_connect import con
from psycopg2._psycopg import cursor
from pprint import pprint

"""
case - когда сы задаем условие
end - окончания условия
when - выражения если чтото то 
then - что будет
else - если не будет выполнено условия when
"""

def case_1():
    with con.cursor() as cur:
        cur: cursor
        cur.execute(
            """
            select
                concat(first_name,' ',last_name),
                length(concat(first_name,' ',last_name)),
                case 
                    when length(concat(first_name,' ',last_name)) > 15
                    then substring(first_name,1,7) || ' ' || substring(last_name,1,7)
                    else concat(first_name,' ',last_name)
                end
            from
                actor;    
            """
        )

        pprint(cur.fetchall())

print(case_1())