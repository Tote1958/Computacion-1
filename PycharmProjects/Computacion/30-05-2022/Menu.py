from Combat_Controller import *
from Constantes import *

menu()
character_controller = Character_Controller()
combat = Combat()
chosen_option = int(input(option_input))
character = 0
enemy = 0
while chosen_option != 100:
    if chosen_option == 1:
        if enemy == 0 and character == 0:
            print(non_combat)
        else:
            combat.combat(character, enemy)
    elif chosen_option == 2:
        character_controller.create_character()
    elif chosen_option == 3:
        character_controller.create_enemy()
    elif chosen_option == 4:
        character_controller.choose_character()
    elif chosen_option == 5:
        enemy = character_controller.choose_enemy()
    elif chosen_option == 6:
        character = character_controller.show_characters()
    elif chosen_option == 7:
        character_controller.show_enemies()

    available_options()
    chosen_option = int(input(option_input))

