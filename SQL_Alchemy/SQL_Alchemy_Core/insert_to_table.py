from SQL_Alchemy.SQL_Alchemy_Core import engine
from models import games


"""Добавления insert через цыкл for"""
games_data = [{'name': 'Game 1', 'price': 1000, 'genre': 'Action'},
              {'name': 'Game 2', 'price': 2000, 'genre': 'Adventure'},
              {'name': 'Game 3', 'price': 500, 'genre': 'Strategy'}]


with engine.connect() as conn:
    for game in games_data:
        conn.execute( games.insert().values( name=game['name'],
                                             price=game['price'],
                                             genre=game['genre'] ) )
    conn.commit()

"""Добавления insert передачей списка словаря"""
games_data_1 = [{'name': 'Game 6', 'price': 1500, 'genre': 'Action'},
              {'name': 'Game 7', 'price': 2020, 'genre': 'Adventure'},
              {'name': 'Game 8', 'price': 359, 'genre': 'Strategy'}]

with engine.connect() as conn:
    conn.execute(games.insert().values(games_data_1))
    conn.commit()

"""Или передать в виде генератора"""

games_data_generator = [('Game 4', 1500, 'Action'), ('Game 5', 2200, 'Adventure'), ('Game 6', 600, 'Strategy')]
game_data_2 = [{'name': name, 'price': price, 'genre': genre} for name, price, genre in games_data_generator]
with engine.connect() as conn:
    conn.execute( games.insert().values( game_data_2) )
    conn.commit()

