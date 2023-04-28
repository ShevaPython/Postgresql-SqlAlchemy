from CREATE_CONECT_DATABASE_ENGINE import engine
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
print(session.query(User).all())
# Вызов метода all() на большом объекте результата не очень эффективен.
# Вместо этого стоит использовать цикл for для перебора по объекту Query
for user in session.query(User):
    print(user.name,user.age,user.status,sep='-')

"""count() возвращает количество элементов в результате"""
print(session.query(Wallet).count())
print('___________')

"""first() возвращает первый результат запроса или None, если последний не вернул данных."""
print(session.query(Wallet.user_id).first())
print('___________')

"""get() возвращает экземпляр с соответствующим первичным ключом или None, если такой объект не был найден."""
print(session.get(User,1))
print('__________')

"""Этот метод позволяет отфильтровать результаты, добавив оператор WHERE.
 Он принимает колонку, оператор и значение. Например:"""
print(session.query(User).filter(User.name == "sss"))
print('___________')