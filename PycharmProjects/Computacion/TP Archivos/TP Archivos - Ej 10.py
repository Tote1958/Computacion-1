class ListProgram:
    def __init__(self, file):
        self.file = file

    def linesNum(self, file, word):
        global list
        list = []
        with open(file, "r") as file:
            list = file.readlines()
            if word in list:
                print(len(list))


archive = ListProgram("C:/Users/jorge/PycharmProjects/Computacion/TP Archivos/TP Archivos - Ej 10 - Archivo.txt")
words = str(input("Ingrese un texto a encontrar: "))
print("El texto ingresado esta en la linea", archive.linesNum(archive.file, words))
