from models.data import users
from utils.crud import show_users


def update_user(users)-> None:
    kogo_szukasz=input("Kogo szukasz?:")
    for user in users:
        if user['name']==kogo_szukasz:
            user['name']=input("Podaj nowe imię:")
            user['surname']=input("Podaj nowe nazwisko:")
            user['posts']=input("Podaj liczbę postów:")
print(users)
update_user(users)
print(users)