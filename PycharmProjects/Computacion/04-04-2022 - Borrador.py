class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def walk(self):
        print(self.name, "is walking")
    def __str__(self):
        return f"nombre: {self.name}"


vikingo = Person("Santino", 19)
vikingo2 = Person("Franco", 23)
vikingo3 = Person("Dante", 20)
lista = [vikingo, vikingo2, vikingo3]

print(lista)


