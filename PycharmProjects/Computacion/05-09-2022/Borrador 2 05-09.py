
class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]

    def hash_function(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 10

    def add(self, key, value):
        h = self.hash_function(key) #llama a la otra funcion, le pasamos la ley, efectua la funcion, se guarda en h
        for i in range(len(self.arr)):
            for n in range(len(self.arr[i])):
                if self.arr[n[0]] == key:
                    i == (key, value)
        if self.arr[h] == []:
            self.arr[h].append((key, value))
        else:
            self.arr[h].append((key, value))


    def print(self):
        print(self.arr)

    def getitem(self, key):
        h = self.hash_function(key)
        for i in self.arr:
            for n in self.arr[i]:
                if n[0] == key:
                    i == (key, )
        return self.arr[h]


program = HashTable()
program.add("lunes", 320)
program.add("senul", 970)
program.print()
program.getitem