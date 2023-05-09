from SQL_Alchemy.SQL_Alchemy_Core import engine
from models import games,developers,publishers

game_1 = {'name': 'World of Warcraft', 'description': """World of Warcraft (WoW; с англ. — «Мир военного ремесла»)
 — массовая многопользовательская ролевая онлайн-игра, разработанная и издаваемая компанией Blizzard Entertainment.
  Действие World of Warcraft происходит в фэнтезийной вселенной Warcraft. Игра тесно связана с предыдущими играми серии 
  — стратегиями в реальном времени; каждый игрок управляет одним персонажем и может взаимодействовать с другими игроками
   в общем виртуальном мире. Игра была анонсирована в 2001 году и выпущена 23 ноября 2004 года, к 10-летней годовщине Warcraft: Orcs & Humans.
World of Warcraft предоставляется игрокам на основе ежемесячной платной подписки; кроме того, для игры регулярно
 выпускаются тематические платные дополнения, добавляющие в игру новые области, новые классы персонажей и иной
  дополнительный или обновлённый контент. На 2020 год было выпущено восемь таких дополнений — The Burning Crusade (2007)
  , Wrath of the Lich King (2008), Cataclysm (2010), Mists of Pandaria (2012), Warlords of Draenor (2014), Legion (2016),
   Battle for Azeroth (2018), Shadowlands (2020) и Dragonflight (2022). В 2019 году также была выпущена версия игры под названием Classic""",
              'price':1000,
              'developer_id':1,
              'publisher_id':1}

developer_1={'name':'Blizzard Entertainment',
              'description':"""Blizzard Entertainment (сокр. Blizzard) — американский разработчик и издатель компьютерных игр """,
              'developer_site':'https://www.blizzard.com/ru-ru/'}
publisher_1={'name':'Blizzard Entertainment',
              'description':"""Blizzard Entertainment (сокр. Blizzard) — американский разработчик и издатель компьютерных игр.
                """,
              'publisher_site':'https://www.blizzard.com/ru-ru/'}
with engine.connect() as conn:
    try:
        conn.execute(publishers.insert().values(publisher_1))
        conn.commit()

        conn.execute( developers.insert().values( developer_1 ) )
        conn.commit()

        conn.execute(games.insert().values(game_1))
        conn.commit()

        print("Запись добавлена")
    except Exception as e:
        print(F'Ошибка:{e}')