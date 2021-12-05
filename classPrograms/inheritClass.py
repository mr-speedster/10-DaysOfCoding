class Animal:
    def __init__(self):
        print("It's a Animal")
class Dog(Animal):
    def justPrint(self):
        print("It's a Dog")
dog=Dog()
dog.justPrint()