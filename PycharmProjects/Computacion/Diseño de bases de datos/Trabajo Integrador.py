import os
import pymysql


def menu():
    """
    Función que limpia la pantalla y muestra nuevamente el menu
    os.system('clear')
    Si el sistema es Windows se usa cls de otro modo se usa clear
    os.name trae el nombre del kernel. NT para windows y POSIX para Mac o Linux
    " ┌ ─ ┐ │ └ ─ ┘ " ├┤
    """
    borrar = 'cls' if os.name == 'nt' else 'clear'
    os.system(borrar)
    print("\t")
    print("┌──────────────────────┐")
    print("│Seleccione su opción │")
    print(" ────────────────────── ")
    print("│ 1 - Cargar producto │")
    print("│ 2 - ABM de clientes │")
    print("│ 3 - Opción Tres │")
    print("│ 9 - Para salir │")
    print("└──────────────────────┘")
    print(" ☺ ")
    print("┌───────────────────────┐")
    print("│ Indica opción elegida │")
    print("└───────────────────────┘")


def opcion1(cursor):
    cursor.execute()


def opcion2():
    print("┌──────────────────────┐")
    print("│Seleccione su opción │")
    print(" ────────────────────── ")
    print("│ 1 -  │")
    print("│ 2 - Opción Dos │")
    print("│ 3 - Opción Tres │")
    print("│ 9 - Para salir │")
    print("└──────────────────────┘")


while True:
    # Mostramos el menu
    menu()
    db = pymysql.connect(host="127.0.0.1", user="root", passwd="43664152a", db="sakila")
    cursor = db.cursor()
    # solicituamos una opción al usuario
    opcionMenu = input()
    if opcionMenu=="1":
        print ("")
        input("Has pulsado la opción 1...\npulsa una tecla para continuar")
        opcion1(cursor)
    elif opcionMenu=="2":
        print ("")
        input("Has pulsado la opción 2...\npulsa una tecla para continuar")
    elif opcionMenu=="3":
        print ("")
        input("Has pulsado la opción 3...\npulsa una tecla para continuar")
    elif opcionMenu=="9":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
