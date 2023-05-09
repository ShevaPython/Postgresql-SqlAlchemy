from sqlalchemy import create_engine
from datta.settings import POSTGRES_URI_Alchemy_Core

# Создание объекта движка базы данных
engine = create_engine(POSTGRES_URI_Alchemy_Core,echo=True)


