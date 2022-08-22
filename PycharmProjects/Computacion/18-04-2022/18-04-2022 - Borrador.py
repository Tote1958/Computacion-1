class Person:
    def __init__(self, name, age):
        self.__name = name if self.check_validate_name(name) else 0
        self.__age = age if self.check_validate_age(age) else 0

    def check_validate_age(self, age):
        if age > 0:
            return True
        else:
            print("La edad ingresada es incorrecta")

    def get_name(self):
        return self.__name

    def check_validate_name(self, name):
        if isinstance(name, str):
            return True
        else:
            print("El nombre ingresado no es una cadena de caracteres")

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age if self.check_validate_age(age) else 0

    def set_name(self, name):
        self.__name = name if self.check_validate_name(name) else 0


vikingo = Person("santno", 50)
print(vikingo.get_age())
print(vikingo.get_name())
