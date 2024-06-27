from abc import ABC

class Person(ABC):
    def __init__(self, f_name, colour):
        ABC.__init__(self, colour)
        self.f_name = f_name

    def __repr__(blarg):
        return f"Name: {blarg.f_name}."

    def printname(self):
        return f"Name is {self.f_name}."

person1 = Person("Tim")
person2 = Person("Dave")

var1 = "Hello"
print(person1)
print(person2.f_name)