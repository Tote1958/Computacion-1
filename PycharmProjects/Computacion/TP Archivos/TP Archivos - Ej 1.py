class Read:
    def reading(self):
        with open("C:/Users/jorge/PycharmProjects/Computacion/TP Archivos - Ej 1 - Archivo.txt","r") as file:
            for line in file:
                print(line)

file = Read()
file.reading()