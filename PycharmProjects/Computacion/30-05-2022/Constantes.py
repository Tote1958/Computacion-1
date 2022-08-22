char_max_stats = 15
en_max_stats = 10
char_limit_reached = "Ya alcanzo el limite de personajes"
en_limit_reached = "Ya alcanzo el limite de enemigos"
max_stats_reached ="Usted ingreso una cantidad mayor a 15, reingrese los puntos"
more_stats_needed = "Usted ingreso una cantidad menor a 15, reingrese los puntos"
name_input = "Ingrese el nombre del personaje: "
age_input = "Ingrese la edad del personaje: "
strength_input = "Ingrese la fuerza del personaje: "
agi_input = "Ingrese la agilidad del personaje: "
con_input = "Ingrese la constitucion del personaje: "
type_input = "Ingrese el tipo de personaje: "
choose_char_input = "Ingrese el indice del personaje elegido: "
available_char = "Los personajes a elegir son: "
available_en = "Los enemigos a elegir son: "
reintroduce_char = "Ingrese un indice valido: "
option_input ="\033[;2m" + "Elija una opcion: "
en_creation = "-- Para la creacion de un enemigo, la cantidad total de tributos debe ser 10 --"
char_creation = "-- Para la creacion de un personaje, la cantidad total de tributos debe ser 15 --"
non_available_char = "No hay personajes creados"
non_available_en = "No hay enemigos creados"
non_combat = "No ha elegido personaje o enemigo"

def menu():
    print("\033[;31m" +"---------------------------------")
    print("\033[;2m" + "*** Bienvenido a WOW trucho ***")
    print("\033[;36m" + "  Opcion 1: Combatir")
    print("\033[;36m" + "  Opcion 2: Crear un personaje")
    print("\033[;36m" + "  Opcion 3: Crear un enemigo")
    print("\033[;36m" + "  Opcion 4: Elegir personaje")
    print("\033[;36m" + "  Opcion 5: Elegir enemigo")
    print("\033[;36m" + "  Opcion 6: Mostrar personajes")
    print("\033[;36m" + "  Opcion 7: Mostrar enemigos")
    print("\033[;31m" +"---------------------------------")

def available_options():
    print("\033[;31m" +"--------------------------------")
    print("\033[;2m" + "        +++ Opciones +++")
    print("\033[;36m" + "  Opcion 1: Combatir")
    print("\033[;36m" + "  Opcion 2: Crear un personaje")
    print("\033[;36m" + "  Opcion 3: Crear un enemigo")
    print("\033[;36m" + "  Opcion 4: Elegir personaje")
    print("\033[;36m" + "  Opcion 5: Elegir enemigo")
    print("\033[;36m" + "  Opcion 6: Mostrar personajes")
    print("\033[;36m" + "  Opcion 7: Mostrar enemigos")
    print("\033[;31m" +"--------------------------------")