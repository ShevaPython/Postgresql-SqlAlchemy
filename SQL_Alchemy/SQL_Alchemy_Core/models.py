from sqlalchemy import  Table, Column, Integer, String, Date, Float, ForeignKey,MetaData,TEXT,func
from SQL_Alchemy.SQL_Alchemy_Core import engine

#Создания обьэкта метаданных
metadata = MetaData()

#Создание таблиц

publishers = Table('publishers', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255),nullable=False),
    Column('description', TEXT,nullable=False),
    Column('publisher_site', String(255),nullable=True)
)

developers = Table('developers', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255),nullable=False),
    Column('description', TEXT,nullable=False),
    Column('developer_site', String(255),nullable=True)
)

games = Table('games', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255),nullable=False),
    Column('description',TEXT,nullable=False),
    Column('price', Float,nullable=False),
    Column('developer_id', Integer, ForeignKey('developers.id')),
    Column('publisher_id', Integer, ForeignKey('publishers.id'))
)

genres = Table('genres', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255),nullable=False)
)

games_genres = Table('games_genres', metadata,
    Column('game_id', Integer, ForeignKey('games.id'), primary_key=True),
    Column('genre_id', Integer, ForeignKey('genres.id'), primary_key=True)
)

clients = Table('clients', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255),nullable=False),
    Column('surname', String(255),nullable=False),
    Column('nickname', String(255),unique=True,nullable=False),
    Column('date_of_registration', Date,default=func.now()),
    Column('online_wallet', Float,default=0)
)

orders = Table('orders', metadata,
    Column('id', Integer, primary_key=True),
    Column('client_id', Integer, ForeignKey('clients.id')),
    Column('order_date', Date),
    Column('total_price', Float,nullable=False)
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


# metadata.drop_all(engine)
metadata.create_all(engine)


