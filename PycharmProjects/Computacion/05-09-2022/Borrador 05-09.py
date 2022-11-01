
class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [None for i in range(self.max)]

    def hash_function(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 10

    def add(self, key, value):
        h = self.hash_function(key) #llama a la otra funcion, le pasamos la ley, efectua la funcion, se guarda en h
        self.arr[h] = value

    def print(self):
        print(self.arr)

    def getitem(self, key):
        h = self.hash_function(key)
        return self.arr[h]

program = HashTable()
program.add("lunes", 320)
program.print()
program.getitem()