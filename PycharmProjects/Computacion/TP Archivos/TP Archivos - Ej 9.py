class ListProgram:
    def __init__(self, file):
        self.file = file

    def linesNum(self, file):
        global list
        list = []
        with open(file, "r") as file:
            for line in file:
                list.append(line)
        return len(list)

    def charactersNum(self,file):
        with open(file, "r") as text:
            data = text.read().replace(" ", "")
            charactersNum = len(data)
        return charactersNum

    def wordsNum(self, file):
        with open(file, "r") as text:
            readText = text.read()
            words = readText.split()
            wordsTotal = len(words)
        return wordsTotal


archive = ListProgram("C:/Users/jorge/PycharmProjects/Computacion/TP Archivos/TP Archivos - Ej 9 - Archivo.txt")
print("El archivo tiene", archive.linesNum(archive.file), "lineas")
print("El archivo tiene", archive.charactersNum(archive.file), "letras")
print("El archivo tiene", archive.wordsNum(archive.file), "palabras")

