import traceback
from SQL_Alchemy.SQL_Alchemy_Core import engine
from models import games, developers, publishers

# Создание издателя
publisher = {
    "name": "Activision Blizzard",
    "description": "American video game holding company based in Santa Monica, California.",
    "publisher_site": "https://www.activisionblizzard.com/"
}

# Создание разработчика
developer = {
    "name": "Blizzard Entertainment",
    "description": "American video game developer based in Irvine, California.",
    "developer_site": "https://www.blizzard.com/"
}

# Игра
game = {
    "name": "World of Warcraft",
    "description": "Massively multiplayer online role-playing game (MMORPG) released in 2004.",
    "price": 15.0
}
with engine.connect() as conn:
    with conn.begin() as trans:
        try:
            # Добавление издателя
            result = conn.execute( publishers.insert().values( **publisher ) )
            publisher_id = result.inserted_primary_key[0]

            # Добавление разработчика
            result = conn.execute( developers.insert().values( **developer ) )
            developer_id = result.inserted_primary_key[0]

            # Добавление игры
            game["developer_id"] = developer_id
            game["publisher_id"] = publisher_id
            result = conn.execute( games.insert().values( **game ) )

        except Exception:
            print( traceback.format_exc() )

    conn.close()
