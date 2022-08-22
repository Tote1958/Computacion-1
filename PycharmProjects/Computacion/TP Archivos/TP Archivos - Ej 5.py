class ListProgram:
    def __init__(self, file):
        self.file = file

    def copy(self,file, newFile):
        global list
        list = []
        with open(file, "r") as file:
            for line in file:
                list.append(line)
        with open(newFile, "w") as secondFile:
            secondFile.writelines(list)
            secondFile.close()


archive = ListProgram("C:/Users/jorge/PycharmProjects/Computacion/TP Archivos/TP Archivos - Ej 5 - Archivo.txt")
archive.copy(archive.file, "C:/Users/jorge/PycharmProjects/Computacion/TP Archivos/TP Archivos - Ej 5 - Archivo 2.txt")
print(list)


