class Animal:
    def __init__(self):
        self.legs = 4

    def breath(self):
        print("Breathing...")

class Dog(Animal):
    def __init__(self):
        super().__init__()

    def bark(self):
        print("woof woof")

