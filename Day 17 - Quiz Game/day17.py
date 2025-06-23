class Car:
    pass #The pass keyword helps if we create a class or function and don't put any code inside then it prevents error

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

#Without Constructor
# user_1 = User()
# user_1.id = "001"
# user_1.username = "Harsh"
# print(user_1.id)
# print(user_1.username)

#With Constructor
user_2 = User("002", "Jack")
print(user_2.id)
print(user_2.username)

user_3 = User("003", "Oggy")

#Default Values in Initializer
print(user_2.followers)
print(user_3.followers)

#Methodss
user_2.follow(user_3)
