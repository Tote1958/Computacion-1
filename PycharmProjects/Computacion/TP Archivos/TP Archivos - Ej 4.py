class ListProgram:
    def __init__(self, file):
        self.file = file

    def save(self,file):
        global list
        list = []
        with open(file, "r") as file:
            for line in file:
                list.append(line)
        return list


archive = ListProgram("C:/Users/jorge/PycharmProjects/Computacion/TP Archivos/TP Archivos - Ej 4 - Archivo.txt")
archive.save(archive.file)
print(list)



