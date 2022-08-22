class Read:

    def __init__(self):
        self.num = 0

    def set_num(self):
        num = int(input("Ingrese el numero de lineas a leer:"))
        self.num = num
        self.reading(self.num)

    def reading(self, num):
        with open("C:/Users/jorge/PycharmProjects/Computacion/TP Archivos/TP Archivos - Ej 2 - Archivo.txt","r") as file:
            for i in range(num):
                print(file.readline())


file = Read()
file.set_num()
