# Create a class called Dog with two instance variables: name and age.
# Add an __init__ method to initialize these variables.
# Also, add a method called bark that prints "Woof, woof!".


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof, woof!")


my_dog = Dog("Gemma", 15)
my_dog.bark()
