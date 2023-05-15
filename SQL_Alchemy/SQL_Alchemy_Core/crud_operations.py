from SQL_Alchemy.SQL_Alchemy_Core import engine
from SQL_Alchemy.SQL_Alchemy_Core.models import clients

with engine.connect() as conn:
    conn.execute(clients.insert().values(name='John Doe', email='john@example.com'))
# Чтение записи:

# получаем пользователя с id=1
result = conn.execute(clients.select().where(clients.c.id == 1))

# выводим имя пользователя
for row in result:
    print(row.name)
# Обновление
# записи:
# обновляем email пользователя с id=1
conn.execute(clients.update().where(clients.c.id == 1).values(email='new_email@example.com'))
# Удаление
# записи:

# удаляем пользователя с id=1
conn.execute(clients.delete().where(clients.c.id == 1))
