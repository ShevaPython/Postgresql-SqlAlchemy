from db_connect import con
from psycopg2._psycopg import cursor
from pprint import pprint
from psycopg2 import Error

"""
Хранения чисел в таблице:
smallint- 2 byte -32 768 до 32 768 
int- 4 byte -2 147 483 684 до 2 147 483 684 
bigint - 8 byte -9 милиарда до  9 милиарда

Хранения строк в таблице:
char - имеет фиксированую длину char(5) если введеные даные будут к примеру 3   произведеться автозаполнения пробелами
varchar - varchar(20) не более 20 чимволов
text - хранения строки до 1 гб

Хранения чисел с плавающей точкой в таблице:
float
double precision
Первые два типа округляют значения и могут привести к ошибкам с опирацией например деньгами

decimal(n,m)   1 234 567. 890 decimal(10,3)

Хранения даты и времени в таблице:
date - хранения даты
timestamp - хранения даты и времени
time - хранения только время
interval -

internet_customer_id SERIAL NOT NULL PRIMARY KEY - создание первичного ключа
"""
con.autocommit = True  # автокомит
try:
    with con.cursor() as cur:
        """
        Удаления таблиц
        """

        cur: cursor
        cur.execute(
            '''
            drop table internet_customer;

            '''

        )
        print("Таблица успешно удалена PostgreSQL")

    print("__________")

    with con.cursor() as cur:
        """
        Создания таблицы
        """

        cur: cursor
        cur.execute(
            '''
            create table internet_customer(
            internet_customer_id SERIAL NOT NULL PRIMARY KEY,
            login VARCHAR(20) not null,
            first_name VARCHAR(50) not null ,
            last_name VARCHAR(50) not null ,
            patronymic VARCHAR(50) null ,
            rating FLOAT default(0) not null,
            birthday DATE null,
            registered TIMESTAMP DEFAULT(now()) not null ,
            deleted BOOLEAN DEFAULT(FALSE) not null 
            
            );
            
            '''

        )
        print("Таблица успешно создана в PostgreSQL")

    print("_____________")

    with con.cursor() as cur:
        cur: cursor
        """
        Заполнения таблиц
        """

        cur.execute("""INSERT INTO internet_customer(login,first_name,last_name ,patronymic,birthday)
                    SELECT 
                        substring(a.first_name,1,1) || '.' || a.last_name,
                        a.first_name,
                        a.last_name,
                        null,
                        null
                    FROM 
                       actor a""")
        cur.execute("""INSERT INTO internet_customer(login,first_name,last_name ,patronymic,birthday)
                                                        VALUES ('login1', 'Коля', 'Abramov', NULL, '1987-01-22'),
                                                               ('login2', 'Nastia', 'Gon4a', NULL, '1987-01-20');"""
                    )

        print("Записи добавлены")
        print("____________")
        with con.cursor() as cur:
            cur: cursor
            """
            Дополняем колонку к существуещей таблице
            """
            cur.execute("""ALTER TABLE internet_customer ADD COLUMN confirmed BOOLEAN DEFAULT(FALSE) NOT NULL ;"""
                        )
            # cur.execute("""ALTER TABLE internet_customer DROP COLUMN confirmed  ;"""
            #             ) удаления колонки
            print("Колонка добавлена")
            print("_______")

            with con.cursor() as cur:
                cur: cursor
                """
                Удаления записи из таблицы
                """
                cur.execute("""
                DELETE FROM internet_customer
                WHERE first_name = 'Nastia';
                """)
                print("Запись удалена")
                print("_______")

                with con.cursor() as cur:
                    cur: cursor
                    """
                    Редактирование записи
                    """
                    cur.execute("""
                    UPDATE internet_customer
                    SET login='testlogin'
                    WHERE first_name='Коля';
                    """)
                    print("Запись изменина")
                    print("_______")

        '''выборка из базы даных'''
        with con.cursor() as cur:
            cur: cursor
            cur.execute(
                '''
                select
                    *
                from
                    internet_customer;     
                '''

            )
            print(cur.fetchall())

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if con:
        con.close()
        print("База даных закрыта")
