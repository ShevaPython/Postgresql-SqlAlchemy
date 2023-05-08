from SQL_Alchemy_ORM import engine
from sqlalchemy.orm import sessionmaker

from SQL_Alchemy import User, Wallet

"""
Метод	Описание
all()	Возвращает результат запроса (объект Query) в виде списка
count()	Возвращает общее количество записей в запросе
first()	Возвращает первый результат из запроса или None, если записей нет
scalar()	Возвращает первую колонку первой записи или None, если результат пустой. Если записей несколько, то бросает исключение MultipleResultsFound
one	Возвращает одну запись. Если их несколько, бросает исключение MutlipleResultsFound. Если данных нет, бросает NoResultFound
get(pk)	Возвращает объект по первичному ключу (pk) или None, если объект не был найден
filter(*criterion)	Возвращает экземпляр Query после применения оператора WHERE
limit(limit)	Возвращает экземпляр Query после применения оператора LIMIT
offset(offset)	Возвращает экземпляр Query после применения оператора OFFSET
order_by(*criterion)	Возвращает экземпляр Query после применения оператора ORDER BY
join(*props, **kwargs)	Возвращает экземпляр Query после создания SQL INNER JOIN
outerjoin(*props, **kwargs)	Возвращает экземпляр Query после создания SQL LEFT OUTER JOIN
group_by(*criterion)	Возвращает экземпляр Query после добавления оператора GROUP BY к запросу
having(criterion)	Возвращает экземпляр Query после добавления оператора HAVING
"""

Session = sessionmaker(bind=engine)
session = Session()
