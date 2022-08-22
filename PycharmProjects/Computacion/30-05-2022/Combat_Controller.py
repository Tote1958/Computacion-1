from random import randint
from Character_Controller import *
from Constantes import *


class Combat():
    def combat(self, chosen_character, chosen_enemy):
        while chosen_character.get_con() != 0 and chosen_enemy != 0:
            dice1 = randint(1, 6)
            dice2 = randint(1, 6)
            randomnumber = dice1 + dice2
            if randomnumber <= 3:
                damage = 0
            elif 4 <= randomnumber <= 6:
                damage = 1
            elif 7 <= randomnumber <= 9:
                damage = 2
            elif 10 <= randomnumber <= 11:
                damage = 3
            elif randomnumber == 12:
                damage = 4


