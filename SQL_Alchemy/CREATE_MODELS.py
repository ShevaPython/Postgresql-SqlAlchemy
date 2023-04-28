from sqlalchemy.orm import relationship
from sqlalchemy import Table, Index, Integer, String, Column, Text, \
    DateTime, Boolean, PrimaryKeyConstraint, \
    UniqueConstraint, ForeignKeyConstraint, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime

from CREATE_CONECT_DATABASE_ENGINE import engine



"""
Создание моделей

Модель — это класс Python, соответствующий таблице в базе данных, а его свойства — это колонки.

Чтобы класс был валидной моделью, нужно соответствовать следующим требованиям:

1.Наследоваться от декларативного базового класса с помощью вызова функции declarative_base().
2.Объявить имя таблицы с помощью атрибута __tablename__.
3.Объявить как минимум одну колонку, которая должна быть частью первичного ключа.
"""

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    photo = Column(String(200), nullable=False)
    status = Column(String(20), default='unregister')
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    wallet = relationship("Wallet", backref='user', uselist=False)

    """При использовании ORM ключи и ограничения добавляются с помощью атрибута __table_args__."""
    __table_args__ = (
        UniqueConstraint('photo'),
    )

    def __repr__(self):
        return F"{self.id}"


class Wallet(Base):
    __tablename__ = 'wallets'
    id = Column(Integer, primary_key=True)
    sum_wallet = Column(Float, default=0)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return F"{self.id}"


Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)#удаления всех таблиц
