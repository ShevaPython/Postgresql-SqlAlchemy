from CREATE_CONECT_DATABASE_ENGINE import engine
from sqlalchemy.orm import sessionmaker
from CREATE_MODELS import User,Wallet



"""Вставка(добавление) данных"""

# Создание нового пользователя и связанного с ним бумажника
user1 = User(
    name='Сергей',
    age=30,
    photo='12312424543534scsdcs'
)

user2 = User(
    name='Виктория',
    age=28,
    photo='12312424543'

)

new_wallet_user1 = Wallet(sum_wallet=0)
new_wallet_user2 = Wallet(sum_wallet=0)
user1.wallet = new_wallet_user1
user2.wallet=new_wallet_user2

# Добавление объектов в базу данных
Session = sessionmaker(bind=engine)
session = Session()
session.add_all([user1,user2])
session.commit()
session.close()

print("Новый пользователь и бумажник созданы!")





