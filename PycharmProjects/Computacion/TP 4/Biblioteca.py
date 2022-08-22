from Libro import *
from Cliente import *


class Library:
    def __init__(self):
        self.bookList = []
        self.clientList = []
        self.clientsBooks = {}

    def showBooks(self):
        for i in range(len(self.bookList)):
            print(self.bookList[i].title)

    def showClients(self):
        for i in range(len(self.clientList)):
            print(self.clientList[i].name)

    def assign(self):
        self.showClients()
        clientIndex = int(input("Ingrese el indice del cliente a asignar: "))
        while clientIndex >= len(self.clientList):
            clientIndex = int(input("Ingrese un indice correcto: "))
        self.showBooks()
        bookIndex = int(input("Ingrese el indice del libro a asignar: "))
        while bookIndex >= len(self.bookList):
            bookIndex = int(input("Ingrese un indice correcto: "))
        if self.clientList[clientIndex] in self.clientsBooks:
            self.clientsBooks[self.clientList[clientIndex]].append(self.bookList[bookIndex])
        else:
            self.clientsBooks[self.clientList[clientIndex]] = self.bookList[bookIndex]


    def showAssignedBooks(self):
        self.showClients()
        clientIndex = int(input("Ingrese el indice del cliente: "))
        while clientIndex >= len(self.clientList):
            clientIndex = int(input("Ingrese un indice correcto: "))
        return self.clientsBooks[self.clientList[clientIndex]]
