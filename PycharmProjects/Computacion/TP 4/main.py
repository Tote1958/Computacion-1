from Biblioteca import *


def createBook():
    bookTitle = str(input("Ingrese el titulo del libro: "))
    bookAuthor = str(input("Ingrese el autor del libro: "))
    bookPrice = float(input("Ingrese el precio del libro: "))
    bookTitle = Book(bookTitle, bookAuthor, bookPrice)
    library.bookList.append(bookTitle)


def createClient():
    clientName = str(input("Ingrese nombre del cliente: "))
    clientAge = int(input("Ingrese la edad del cliente: "))
    clientAdress = str(input("Ingrese la direccion del cliente: "))
    clientName = Client(clientName, clientAge, clientAdress)
    library.clientList.append(clientName)


def viewBooksList():
    if len(library.bookList) == 0:
        print("No hay libros registrados")
        create = str(input("Si desea registrar un libro, escriba si: "))
        create = create.lower()
        if create == "si":
            createBook()
    else:
        library.showBooks()


def viewClientsList():
    if len(library.clientList) == 0:
        print("No hay clientes registrados")
        create = str(input("Si desea registrar un cliente, escriba si: "))
        create = create.lower()
        if create == "si":
            createClient()
    else:
        library.showClients()


def viewBookFromList():
    if len(library.bookList) == 0:
        print("No hay libros registrados")
    else:
        print("Los libros que hay registrados son:")
        library.showBooks()
        bookNum = int(input("Ingrese el indice del libro: "))
        while bookNum >= len(library.bookList):
            bookNum = int(input("Ingrese un indice correcto: "))
        library.bookList[bookNum].viewBook()


def viewClientFromList():
    if len(library.clientList) == 0:
        print("No hay clientes registrados")
    else:
        print("Los clientes que hay registrados son:")
        library.showClients()
        clientNum = int(input("Ingrese el indice del libro: "))
        while clientNum >= len(library.clientList):
            clientNum = int(input("Ingrese un indice correcto: "))
        library.clientList[clientNum].viewClient()


library = Library()
chosenOption = str()
while chosenOption != 6:
    print("Listado de opciones:")
    print("Opcion 1: Ver lista de libros")
    print("Opcion 2: Ver lista de clientes")
    print("Opcion 3: Crear un libro")
    print("Opcion 4: Crear un cliente")
    print("Opcion 5: Ver informacion de un libro")
    print("Opcion 6: Ver informacion de un cliente")
    print("Opcion 7: Asignar un libro a un cliente")
    print("Opcion 8: Ver los que libros tiene asignado cada cliente")
    print("Opcion 9: Apagar ")
    chosenOption = int(input("Ingrese el numero de la opcion elegida: "))
    if chosenOption == 1:
        viewBooksList()
    elif chosenOption == 2:
        viewClientsList()
    elif chosenOption == 3:
        createBook()
    elif chosenOption == 4:
        createClient()
    elif chosenOption == 5:
        viewBookFromList()
    elif chosenOption == 6:
        viewClientFromList()
    elif chosenOption == 7:
        library.assign()
    elif chosenOption == 8:
        print(library.showAssignedBooks())
    elif chosenOption == 9:
        break
    else:
        chosenOption = str(input("La opcion ingresada fue incorrecta, escriba otra valida: "))


