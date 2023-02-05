# What is OOP and why?

# Class and Object, attributes and method

# turtle https://docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen
timmy = Turtle()

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# pretty table
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("name", ["a", "b", "c"])
table.add_column("type", ["a", "b", "c"])
print(table)

# Extras: PascalCase, camelCase, snake_case

# Creating our own class
class User():
    pass

user1 = User()
user1.id = "001"
user1.name = "pan"

# Constructor and attributes initialization
class UserWithConstructor():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.follower = 0

user2 = UserWithConstructor("002", "tee")

class UserWithConstructorAndMethod():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.follower = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.follower += 1

    def print_details(self):
        print(f"id: {self.id}, name: {self.name}, follwer count: {self.follower}, following count: {self.following}")

user3 = UserWithConstructorAndMethod("003", "pan")
user4 = UserWithConstructorAndMethod("004", "tee")

user3.follow(user4)

user3.print_details()
user4.print_details()