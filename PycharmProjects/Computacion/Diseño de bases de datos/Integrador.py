import os
import pymysql
import time


def menu():
    borrar = 'cls' if os.name == 'nt' else 'clear'
    os.system(borrar)
    print("\t")
    print("┌────────────────────────────┐")
    print("│Seleccione su opción        │")
    print(" ──────────────────────────── ")
    print("│ 1 - Ver tabla de clientes  │")
    print("│ 2 - Ver tabla de productos │")
    print("│ 3 - Ver tabla de pedidos   │")
    print("│ 4 - Ver tabla de deposito  │")
    print("│ 5 - ABM de clientes        │")
    print("│ 6 - ABM de productos       │")
    print("│ 7 - ABM de pedidos         │")
    print("│ 8 - ABM de deposito        │")
    print("│ 9 - Para salir             │")
    print("└────────────────────────────┘")
    print(" ☺ ")
    print("┌───────────────────────┐")
    print("│ Indica opción elegida │")
    print("└───────────────────────┘")


def mostrar_tabla_clientes(cursor):
    cursor.execute(f"SELECT * FROM clientes;")
    data = cursor.fetchall()
    print('ID | Nombre y Apellido |   DNI    | Telefono ')
    for i in range(len(data)):
        print(data[i])
    time.sleep(2)


def mostrar_tabla_productos(cursor):
    cursor.execute(f"SELECT * FROM productos;")
    data = cursor.fetchall()
    print('ID |', 'Nombre ')
    for i in range(len(data)):
        print(data[i])
    time.sleep(2)


def mostrar_tabla_pedidos(cursor):
    cursor.execute(f"SELECT * FROM pedidos;")
    data = cursor.fetchall()
    print('ID | ID cliente |  Estado | Fecha de pedido | Cantidad | Id producto')
    for i in range(len(data)):
        print(data[i])
    time.sleep(2)


def mostrar_tabla_deposito(cursor):
    cursor.execute(f"SELECT * FROM deposito;")
    data = cursor.fetchall()
    print('ID | Cantidad | Id Producto ')
    for i in range(len(data)):
        print(data[i])
    time.sleep(2)


def administrar_clientes(cursor):
    print("┌─────────────────────────┐")
    print("│Seleccione su opción     │")
    print(" ───────────────────────── ")
    print("│ 1 - Crear nuevo cliente │")
    print("│ 2 - Modificar cliente   │")
    print("│ 3 - Borrar cliente      │")
    print("│ 9 - Para salir          │")
    print("└─────────────────────────┘")
    while True:
        opcionMenu = input()
        if opcionMenu == "1":
            print("")
            print("Has pulsado la opción 1...")
            crear_cliente(cursor)
            break
        elif opcionMenu == "2":
            print("")
            print("Has pulsado la opción 2...")
            modificar_cliente(cursor)
            break
        elif opcionMenu == "3":
            print("")
            print("Has pulsado la opción 3...")
            borrar_cliente(cursor)
            break
        elif opcionMenu == "9":
            break
        else:
            print("")
            print("No has pulsado ninguna opción correcta...")


def crear_cliente(cursor):
    nomyape_cliente = str(input("Ingrese el nombre y apellido del cliente: "))
    dni_cliente = str(input("Ingrese el DNI del cliente: "))
    telef_cliente = str(input("Ingrese el telefono del cliente: "))
    cursor.execute(f"INSERT INTO clientes (NomyApe, DNI, Telefono) VALUES('{nomyape_cliente}', '{dni_cliente}', '{telef_cliente}');")
    db.commit()
    db.close()
    print(f"{cursor.rowcount} details inserted")


def modificar_cliente(cursor):
    id_cliente = str(input("Ingrese el id del cliente a modificar: "))
    nomyape_cliente = str(input("Ingrese el nombre y apellido del cliente: "))
    dni_cliente = str(input("Ingrese el DNI del cliente: "))
    telef_cliente = str(input("Ingrese el telefono del cliente: "))
    cursor.execute(f"UPDATE clientes SET NomyApe = '{nomyape_cliente}', DNI = '{dni_cliente}', Telefono = '{telef_cliente}' WHERE idClientes = '{id_cliente}';")
    db.commit()
    db.close()
    print(f"{cursor.rowcount} details inserted")


def borrar_cliente(cursor):
    mostrar_tabla_clientes(cursor)
    id_cliente = str(input("Ingrese el id del cliente a borrar: "))
    cursor.execute(f"DELETE FROM clientes WHERE idClientes = '{id_cliente}'; ")
    db.commit()
    db.close()


def administrar_productos(cursor):
    print("┌────────────────────────┐")
    print("│Seleccione su opción    │")
    print(" ──────────────────────── ")
    print("│ 1 - Crear producto     │")
    print("│ 2 - Modificar producto │")
    print("│ 3 - Borrar producto    │")
    print("│ 9 - Para salir         │")
    print("└────────────────────────┘")
    while True:
        opcionMenu = input()
        if opcionMenu == "1":
            print("")
            print("Has pulsado la opción 1...")
            crear_producto(cursor)
            break
        elif opcionMenu == "2":
            print("")
            print("Has pulsado la opción 2...")
            modificar_producto(cursor)
            break
        elif opcionMenu == "3":
            print("")
            print("Has pulsado la opción 3...")
            borrar_producto(cursor)
            break
        elif opcionMenu == "9":
            break
        else:
            print("")
            print("No has pulsado ninguna opción correcta...")


def crear_producto(cursor):
    nombre_producto = str(input("Ingrese el nombre del producto: "))
    cursor.execute(f"INSERT INTO productos (nombre) VALUES('{nombre_producto}');")
    db.commit()
    print(f"{cursor.rowcount} details inserted")
    db.close()


def modificar_producto(cursor):
    id_producto = str(input("Ingrese el id del producto a modificar: "))
    nombre_producto = str(input("Ingrese el nombre nuevo: "))
    cursor.execute(f"UPDATE productos SET nombre = '{nombre_producto}' WHERE idProductos = '{id_producto}';")
    db.commit()
    db.close()


def borrar_producto(cursor):
    id_producto = str(input("Ingrese el nombre del producto: "))
    cursor.execute(f"DELETE FROM productos WHERE idProductos = '{id_producto}';")
    db.commit()
    db.close()


def administrar_pedidos(cursor):
    print("┌────────────────────────────────┐")
    print("│Seleccione su opción            │")
    print(" ──────────────────────────────── ")
    print("│ 1 - Crear pedido               │")
    print("│ 2 - Borrar pedido              │")
    print("│ 3 - Modificar estado de pedido │")
    print("│ 9 - Para salir                 │")
    print("└────────────────────────────────┘")
    while True:
        opcionMenu = input()
        if opcionMenu == "1":
            print("")
            print("Has pulsado la opción 1...")
            crear_pedido(cursor)
            break
        elif opcionMenu == "2":
            print("")
            print("Has pulsado la opción 2...")
            borrar_pedido(cursor)
            break
        elif opcionMenu == "3":
            print("")
            print("Has pulsado la opción 3...")
            modificar_estado(cursor)
            break
        elif opcionMenu == "9":
            break
        else:
            print("")
            print("No has pulsado ninguna opción correcta...")


def crear_pedido(cursor):
    fecha = time.strftime("%y/%m/%d")
    print("Los clientes registrados son: ")
    mostrar_tabla_clientes(cursor)
    id_cliente = int(input("Ingrese el id del cliente que hizo el pedido: "))
    print("Tabla de productos:")
    mostrar_tabla_productos(cursor)
    print("Tabla de deposito:")
    mostrar_tabla_deposito(cursor)
    id_deposito = int(input("Ingrese el id del producto: "))
    cantidad_pedido = int(input("Ingrese la cantidad: "))

    cursor.execute(f"SELECT Cantidad FROM deposito WHERE idDeposito = '{id_deposito}';")
    data = cursor.fetchone()
    data = data[0]
    print(data)
    if cantidad_pedido <= data:
        cursor.execute(f"INSERT INTO pedidos (Clientes_idClientes, Estado, Fecha_pedido, Cantidad, Deposito_idDeposito)"
                       f"VALUES('{id_cliente}', 'NO ENTREGADO', '{fecha}', '{cantidad_pedido}', '{id_deposito}');")
        cantidad_nueva = data - cantidad_pedido
        cursor.execute(f"UPDATE deposito SET Cantidad = '{cantidad_nueva}' WHERE idDeposito = '{id_deposito}';")
        db.commit()
        db.close()
    else:
        print("No hay cantidad suficiente del producto ingresado en el deposito")


def borrar_pedido(cursor):
    mostrar_tabla_pedidos(cursor)
    id_pedido = str(input("Ingrese el id del pedido a borrar: "))
    cursor.execute(f"DELETE FROM pedidos WHERE idPedidos = '{id_pedido}';")
    db.commit()
    db.close()


def modificar_estado(cursor):
    mostrar_tabla_pedidos(cursor)
    id_pedido = str(input("Ingrese el id del pedido: "))
    cursor.execute(f"UPDATE pedidos SET estado = 'ENTREGADO' WHERE idPedidos = '{id_pedido}';")
    db.commit()
    db.close()


def administrar_deposito(cursor):
    print("┌───────────────────────────┐")
    print("│Seleccione su opción       │")
    print(" ─────────────────────────── ")
    print("│ 1 - Añadir mercaderia     │")
    print("│ 2 - Modificar mercaderia  │")
    print("│ 3 - Borrar mercaderia     │")
    print("│ 9 - Para salir            │")
    print("└───────────────────────────┘")
    while True:
        opcionMenu = input()
        if opcionMenu == "1":
            print("")
            print("Has pulsado la opción 1...")
            crear_mercaderia(cursor)
            break
        elif opcionMenu == "2":
            print("")
            print("Has pulsado la opción 2...")
            modificar_mercaderia(cursor)
            break
        elif opcionMenu == "3":
            print("")
            print("Has pulsado la opción 3...")
            borrar_mercaderia(cursor)
            break
        elif opcionMenu == "9":
            break
        else:
            print("")
            print("No has pulsado ninguna opción correcta...")


def crear_mercaderia(cursor):
    print("Tabla de productos:")
    mostrar_tabla_productos(cursor)
    id_producto = int(input("Ingrese el id del producto: "))
    cantidad = int(input("Ingrese la cantidad: "))
    cursor.execute(f"INSERT INTO deposito (Cantidad, Productos_idProductos) VALUES('{cantidad}', '{id_producto}')")
    db.commit()
    db.close()
    print(f"{cursor.rowcount} details inserted")


def modificar_mercaderia(cursor):
    print("Tabla de deposito: ")
    id_deposito = int(input("Ingrese el id de la mercaderia a modificar: "))
    cantidad = int(input("Ingrese la cantidad nueva: "))
    cursor.execute(f"UPDATE deposito SET Cantidad = '{cantidad}' WHERE idDeposito = '{id_deposito}' ")
    db.commit()
    db.close()
    print(f"{cursor.rowcount} details inserted")


def borrar_mercaderia(cursor):
    mostrar_tabla_deposito(cursor)
    id_deposito = str(input("Ingrese el id del cliente a borrar: "))
    cursor.execute(f"DELETE FROM deposito WHERE idDeposito = '{id_deposito}';")
    db.commit()
    db.close()


while True:
    menu()  # Mostramos el menu
    db = pymysql.connect(host="127.0.0.1", user="root", passwd="43664152a", db="integrador")
    cursor = db.cursor()
    opcionMenu = input()  # solicituamos una opción al usuario
    if opcionMenu == "1":
        print("")
        print("Has pulsado la opción 1...")
        mostrar_tabla_clientes(cursor)
    elif opcionMenu == "2":
        print("")
        print("Has pulsado la opción 2...")
        mostrar_tabla_productos(cursor)
    elif opcionMenu == "3":
        print("")
        print("Has pulsado la opción 3...")
        mostrar_tabla_pedidos(cursor)
    elif opcionMenu == "4":
        print("")
        print("Has pulsado la opción 4...")
        mostrar_tabla_deposito(cursor)
    elif opcionMenu == "5":
        print("")
        print("Has pulsado la opción 5...")
        administrar_clientes(cursor)
    elif opcionMenu == "6":
        print("")
        print("Has pulsado la opción 6...")
        administrar_productos(cursor)
    elif opcionMenu == "7":
        print("")
        print("Has pulsado la opción 7...")
        administrar_pedidos(cursor)
    elif opcionMenu == "8":
        print("")
        print("Has pulsado la opción 8...")
        administrar_deposito(cursor)
    elif opcionMenu == "9":
        db.close()
        break
    else:
        print("")
        print("No has pulsado ninguna opción correcta...")

