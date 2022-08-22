class Program:
    def __init__(self, file):
        self.file = file

    def writing(self):
        file = open("C:/Users/jorge/PycharmProjects/Computacion/TP Archivos/TP Archivos - Ej 3 - Archivo.txt", "w")
        file.write(str(input("Ingrese el texto: ")))
        file.close()

    def reading(self):
        with open("C:/Users/jorge/PycharmProjects/Computacion/TP Archivos/TP Archivos - Ej 3 - Archivo.txt","r") as file:
            for line in file:
                print(line)
file = Program(open("C:/Users/jorge/PycharmProjects/Computacion/TP Archivos/TP Archivos - Ej 3 - Archivo.txt"))
file.writing()
file.reading()