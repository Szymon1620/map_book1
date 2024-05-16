class User:

    def __init__(self, name, surname, posts, location):
        self.name = name
        self.surname = surname
        self.posts = posts
        self.location = location


user_1 = User("Jan", "Borowiecki", "3", "Warszawa")
user_1 = User("Tomek", "Borowiecki", "34", "Warszawa")
print(user_1.name)

