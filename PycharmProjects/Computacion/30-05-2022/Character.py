from Constantes import *


class Character:
    def __init__(self, name, age, str, agi, con, type):
        self.__name = name
        self.__age = age
        self.__str = str
        self.__agi = agi
        self.__con = con
        self.__type = type

    def set_name(self):
        self.__name = str(input(name_input))

    def set_age(self):
        self.__age = int(input(age_input))

    def set_str(self):
        self.__str = int(input(strength_input))

    def set_agi(self):
        self.__agi = int(input(agi_input))

    def set_con(self):
        self.__con = int(input(con_input))

    def set_type(self):
        validate_type = False
        while validate_type == False:
            type = str(input(type_input))
            type = type.lower()
            if type == "humano":
                strength = self.get_str()
                self.__str = strength + 2
                self.__type = type
                validate_type = True
            elif type == "elfo":
                agi = self.get_agi()
                self.__agi = agi + 2
                self.__type = type
                validate_type = True
            elif type == "enano":
                con = self.get_con()
                self.__con = con + 2
                self.__type = type
                validate_type = True

    def __str__(self):
        return f"Nombre: {self.__name} \nEdad: {self.__age} \nFuerza: {self.__str} \nAgilidad: {self.__agi} \nConstitucion: {self.__con} \nTipo: {self.__type}"


    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_agi(self):
        return self.__agi

    def get_str(self):
        return self.__str

    def get_con(self):
        return self.__con

    def get_type(self):
        return self.__type





