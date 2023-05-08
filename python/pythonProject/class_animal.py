class Animal(object):
    def __init__(self, name):
        self.name = name

    def move(self):
        print("move~")

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("woof-woof")

class Duck(Animal):
    def speak(self):
        print("quack-quack")