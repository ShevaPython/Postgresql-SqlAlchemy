from sqlalchemy import MetaData,Column,Integer,String,Table

from SQL_Alchemy.SQL_Alchemy_Core import core_engine

#Создания обьэкта метаданных
metadata = MetaData()

#Создание таблиц

students = Table(
    'students',
    metadata,
    Column('id',Integer,primary_key=True),
    Column('name',String),
    Column('age',Integer)
)

metadata.create_all(core_engine)

#Добавления в таблицу

con = core_engine.connect()
con.execute(students.insert(),[

            {'name':'Сергей','age':20},
            {'name':'vava','age':22},
            {'name':'sdsd','age':23},
            {'name':'asas','age':24}
            ])
