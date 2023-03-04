import psycopg2
from psycopg2._psycopg import connection
from datta import settings


class ConnectPsql():
    connect = None

    @classmethod
    def create_con(cls):
        try:
            cls.connect: connection = psycopg2.connect( dbname=settings.DATABASE,
                                                        user=settings.PGUSER,
                                                        password=settings.PGPASSWORD,
                                                        host=settings.ip )
        except Exception as ex:
            print( "Ошибка подключения к бд", ex )

        return cls.connect


con = ConnectPsql.create_con()