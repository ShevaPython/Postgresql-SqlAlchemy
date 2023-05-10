from sqlalchemy import select, column
from SQL_Alchemy.SQL_Alchemy_Core import engine
from models import games, genres, games_genres

"""Добавить жанр "MMORPG" в таблицу genres и присвоить его игре "World of Warcraft"."""
with engine.connect() as conn:
    with conn.begin() as trans:
        try:
            # Добавляем жанр MMORPG
            conn.execute( genres.insert().values( name="MMORPG" ) )

            # Получаем id жанра MMORPG
            genre_id = conn.execute(
                select( column( 'id' ) ).select_from( genres ).where( genres.c.name == "MMORPG" ) ).scalar()

            # Получаем id игры World of Warcraft
            game_id = conn.execute(select(games.c.id).where(games.c.name == "World of Warcraft")).scalar()
            #
            # Связываем жанр с игрой
            conn.execute( games_genres.insert().values( game_id=game_id, genre_id=genre_id ) )

            trans.commit()

        except:
            trans.rollback()
            conn.close()
            raise
