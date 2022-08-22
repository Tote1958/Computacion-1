"""class Character():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self, age):
        self.__age = age


vikingo = Character("Santino", -20)
print(vikingo.get_name())
age = -100
while age < 0:
    age = int(input("Ingrese la edad: "))
vikingo.set_name(age)
print(vikingo.get_age())
"""
class Character():
    def __init__(self, name, age):
        self.__name = name
        self.set_age(age)
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_age(self, age):
        while age < 0:
            age = int(input("Ingrese la edad: "))
        self.__age = age


vikingo = Character("Santino", -20)
print(vikingo.get_name())

print(vikingo.get_age())