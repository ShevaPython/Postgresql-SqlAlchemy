from sqlalchemy import create_engine, Table, Column, Integer, String, Date, Float, ForeignKey,MetaData,TEXT
from SQL_Alchemy.SQL_Alchemy_Core import engine

#Создания обьэкта метаданных
metadata = MetaData()

#Создание таблиц

publishers = Table('publishers', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('description', TEXT),
    Column('publisher_site', String(255))
)

developers = Table('developers', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('description', TEXT),
    Column('developer_site', String(255))
)

games = Table('games', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('description',TEXT),
    Column('price', Float),
    Column('developer_id', Integer, ForeignKey('developers.id')),
    Column('publisher_id', Integer, ForeignKey('publishers.id'))
)

genres = Table('genres', metadata,
    Column('id', Integer, primary_key=True),
    Column('genre', String(255))
)

games_genres = Table('games_genres', metadata,
    Column('game_id', Integer, ForeignKey('games.id'), primary_key=True),
    Column('genre_id', Integer, ForeignKey('genres.id'), primary_key=True)
)

clients = Table('clients', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('surname', String(255)),
    Column('nickname', String(255)),
    Column('date_of_registration', Date),
    Column('online_wallet', Float)
)

orders = Table('orders', metadata,
    Column('id', Integer, primary_key=True),
    Column('client_id', Integer, ForeignKey('clients.id')),
    Column('order_date', Date),
    Column('total_price', Float)
)

order_products = Table('order_products', metadata,
    Column('order_id', Integer, ForeignKey('orders.id'), primary_key=True),
    Column('game_id', Integer, ForeignKey('games.id'), primary_key=True),
    Column('quantity', Integer),
    Column('price', Float)
)

sales = Table('sales', metadata,
    Column('id', Integer, primary_key=True),
    Column('game_id', Integer, ForeignKey('games.id')),
    Column('client_id', Integer, ForeignKey('clients.id')),
    Column('sale_date', Date),
    Column('price', Float)
)


metadata.drop_all(engine)
metadata.create_all(engine)


