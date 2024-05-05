from models.data import users
from utils.crud import show_users


def remove_user(users)-> None:
    kogo_szukasz=input("Kogo szukasz?:")
    for user in users:
        if user['name']==kogo_szukasz:
            users.remove(user)

search_user(users)
print(users)