from sqlalchemy.exc import IntegrityError
from SQL_Alchemy.SQL_Alchemy_Core import engine
from SQL_Alchemy.SQL_Alchemy_Core.models import developers, publishers, games, genres, games_genres, clients


class CommandShop:

    def __init__(self):
        self.engine = engine

    def add_game(self, name, description, price, developer_name, developer_description,
                 publisher_name, publisher_description, genres_names):
        """
         Add a new game to the database with the given details.

         Parameters:
             name (str): The name of the game.
             description (str): The description of the game.
             price (float): The price of the game.
             developer_name (str): The name of the game developer.
             developer_description (str): The description of the game developer.
             publisher_name (str): The name of the game publisher.
             publisher_description (str): The description of the game publisher.
             genres_names (List[str]): A list of genres that the game belongs to.

         Returns:
             None

         Raises:
             IntegrityError: If there is a data integrity violation.
             Exception: If any other error occurs.
         """
        with engine.connect() as conn:
            trans = conn.begin()
            try:
                # Check if developer exists
                developer = conn.execute(
                    developers.select().where(developers.c.name == developer_name)
                ).fetchone()
                if not developer:
                    # If developer does not exist, add to table
                    developer_values = {
                        'name': developer_name,
                        'description': developer_description
                    }
                    result = conn.execute(developers.insert().values(**developer_values))
                    developer_id = result.inserted_primary_key[0]
                else:
                    developer_id = developer.id

                # Check if publisher exists
                publisher = conn.execute(
                    publishers.select().where(publishers.c.name == publisher_name)
                ).fetchone()
                if not publisher:
                    # If publisher does not exist, add to table
                    publisher_values = {
                        'name': publisher_name,
                        'description': publisher_description
                    }
                    result = conn.execute(publishers.insert().values(**publisher_values))
                    publisher_id = result.inserted_primary_key[0]
                else:
                    publisher_id = publisher.id

                # Add game to table
                game_values = {
                    'name': name,
                    'description': description,
                    'price': price,
                    'developer_id': developer_id,
                    'publisher_id': publisher_id
                }
                result = conn.execute(games.insert().values(**game_values))
                game_id = result.inserted_primary_key[0]

                # Add genres to game_genres table
                for genre_name in genres_names:
                    genre = conn.execute(
                        genres.select().where(genres.c.name == genre_name)
                    ).fetchone()
                    if not genre:
                        # If genre does not exist, add to table
                        genre_values = {
                            'name': genre_name
                        }
                        result = conn.execute(genres.insert().values(**genre_values))
                        genre_id = result.inserted_primary_key[0]
                    else:
                        genre_id = genre.id

                    conn.execute(games_genres.insert().values(game_id=game_id, genre_id=genre_id))

                trans.commit()
                print(f"Game '{name}' has been added successfully!")
            except IntegrityError:
                trans.rollback()
                print("Error: Data integrity violation occurred.")
            except Exception as e:
                trans.rollback()
                print(f"Error: {str(e)}")

    def add_client(self, name: str, surname: str, nickname: str, online_wallet: float):
        """
        Add a new client to the clients table.

        :param name: str Name of the client.
        :param surname: str Surname of the client.
        :param nickname: str Nickname of the client.
        :param online_wallet: float Online wallet balance of the client.
        :return: None if the client is added successfully, otherwise return an error message.
        :raises IntegrityError: If there is a data integrity violation.
        :raises Exception: If any other error occurs.
        """
        # The function implementation here...

        with engine.connect() as conn:
            trans = conn.begin()
            try:
                client = conn.execute(clients.select().where(clients.c.surname == surname)).fetchone()

                if not client:
                    client_value = {
                        'name': name,
                        'surname': surname,
                        'nickname': nickname,
                        'online_wallet': float(online_wallet)
                    }

                    result = conn.execute(clients.insert().values(**client_value))
                    print(f"Client '{name}' has been added successfully!")
                else:
                    print(F"Nick_name already exists,please change nick_name")

                trans.commit()


            except IntegrityError:
                trans.rollback()
                print("Error: Data integrity violation occurred.")
            except Exception as e:
                trans.rollback()
                print(f"Error: {str(e)}")


# add_game(
#     name="Game Name",
#     description="Game Description",
#     price=29.99,
#     developer_name="Developer Name",
#     developer_description="Developer Description",
#     publisher_name="Publisher Name",
#     publisher_description="Publisher Description",
#     genres_names=["Action", "Adventure", "RPG"]
# )

# kolia = CommandShop()
# kolia.add_client('Коля', 'Шмедюк', 'smedk', online_wallet=20)
