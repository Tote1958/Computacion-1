from Character import *
from Constantes import *


class Character_Controller:
    def __init__(self):
        self.characters_list = []
        self.enemies_list = []
        se

    def create_character(self):
        if len(self.characters_list) == 2:
            return char_limit_reached
        name = str(input(name_input))
        age = int(input(age_input))
        strength = int(input(strength_input))
        agi = int(input(agi_input))
        con = int(input(con_input))
        stats = strength + agi + con
        while stats < char_max_stats:
            print(more_stats_needed)
            strength = int(input(strength_input))
            agi = int(input(agi_input))
            con = int(input(con_input))
            stats = strength + agi + con
        while stats > char_max_stats:
            print(max_stats_reached)
            strength = int(input(strength_input))
            agi = int(input(agi_input))
            con = int(input(con_input))
            stats = strength + agi + con
        validate_type = False
        while validate_type == False:
            global type
            type = str(input(type_input))
            type = type.lower()
            if type == "humano":
                strength = strength + 2
                validate_type = True
            elif type == "elfo":
                agi = agi + 2
                validate_type = True
            elif type == "enano":
                con = con + 2
                validate_type = True
        creating_character = Character(name, age, strength, agi, con, type)
        self.characters_list.append(creating_character)

    def create_enemy(self):
        name = str(input(name_input))
        age = int(input(age_input))
        strength = int(input(strength_input))
        agi = int(input(agi_input))
        con = int(input(con_input))
        stats = strength + agi + con
        while stats < en_max_stats:
            print(more_stats_needed)
            strength = int(input(strength_input))
            agi = int(input(agi_input))
            con = int(input(con_input))
            stats = strength + agi + con
        while stats > en_max_stats:
            print(max_stats_reached)
            strength = int(input(strength_input))
            agi = int(input(agi_input))
            con = int(input(con_input))
            stats = strength + agi + con
        validate_type = False
        while validate_type == False:
            global type
            type = str(input(type_input))
            type = type.lower()
            if type == "humano":
                strength = strength + 2
                validate_type = True
            elif type == "elfo":
                agi = agi + 2
                type = True
            elif type == "enano":
                con = con + 2
                validate_type = True
        creating_enemy = Character(name, age, strength, agi, con, type)
        self.enemies_list.append(creating_enemy)

    def choose_character(self):
        global chosen_character
        print(available_char)
        for i in range(len(self.characters_list)):
            print(self.characters_list[i].get_name())
        chosen_character = int(input(choose_char_input))
        while chosen_character not in range(len(self.characters_list)):
            chosen_character = int(input(reintroduce_char))
        chosen_character = self.characters_list[chosen_character]
        print("El personaje elegido es:", chosen_character.get_name())
        return chosen_character

    def choose_enemy(self):
        global chosen_enemy
        if len(self.characters_list) == 0:
            return non_available_en
        print(available_en)
        for i in range(len(self.enemies_list)):
            print(self.enemies_list[i].get_name())
        chosen_enemy = int(input(choose_char_input))
        while chosen_enemy not in range(len(self.enemies_list)):
            chosen_enemy = int(input(reintroduce_char))
        chosen_enemy = self.enemies_list[chosen_enemy]
        print("El personaje elegido es:", chosen_enemy.get_name())
        return chosen_enemy

    def show_characters(self):
        print(available_char)
        for i in range(len(self.characters_list)):
            print(self.characters_list[i].get_name())

    def show_enemies(self):
        print(available_char)
        for i in range(len(self.enemies_list)):
            print(self.enemies_list[i].get_name())