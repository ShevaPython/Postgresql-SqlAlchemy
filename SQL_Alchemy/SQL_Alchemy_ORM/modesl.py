from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from SQL_Alchemy.SQL_Alchemy_ORM import engine

"""
Создание моделей

Модель — это класс Python, соответствующий таблице в базе данных, а его свойства — это колонки.

Чтобы класс был валидной моделью, нужно соответствовать следующим требованиям:

1.Наследоваться от декларативного базового класса с помощью вызова функции declarative_base().
2.Объявить имя таблицы с помощью атрибута __tablename__.
3.Объявить как минимум одну колонку, которая должна быть частью первичного ключа.
"""


class Base( DeclarativeBase ):
    pass


class User( Base ):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column( primary_key=True )
    name: Mapped[str] = mapped_column( String( 30 ) )
    fullname: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address( Base ):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column( primary_key=True )
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column( ForeignKey( "user_account.id" ) )
    user: Mapped["User"] = relationship( back_populates="addresses" )

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


#
Base.metadata.create_all( engine )
Base.metadata.drop_all( engine )  # удаления всех таблиц
