import sqlalchemy
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from datta import settings

"""
Дополнительные аргументы
В следующей таблице перечислены дополнительные аргументы-ключевые слова, которые можно передать в функцию create_engine().

Аргумент	Описание
echo	-Булево значение. Если задать True, то движок будет сохранять логи SQL в стандартный вывод. По умолчанию значение равно False
pool_size-	Определяет количество соединений для пула. По умолчанию — 5
max_overflow-	Определяет количество соединений вне значения pool_size. По умолчанию — 10
encoding-	Определяет кодировку SQLAlchemy. По умолчанию — UTF-8. Однако этот параметр не влияет на кодировку всей базы данных
isolation_level-	Уровень изоляции. Эта настройка контролирует степень изоляции одной транзакции.
                Разные базы данных поддерживают разные уровни. Для этого лучше ознакомиться с документацией конкретной базы данных
"""

print(sqlalchemy.__version__)

from sqlalchemy import create_engine

# Подключение к серверу PostgreSQL на localhost с помощью psycopg2 DBAPI
engine = create_engine(
    F"postgresql+psycopg2://{settings.NAME_PGUSER_SQLALCHEMY}:{settings.PGPASSWORD}@{settings.ip}/{settings.SQL_ALCHEMY_DATABASE}",
    echo=True, pool_size=6, max_overflow=10)
engine.connect()
print(engine)
