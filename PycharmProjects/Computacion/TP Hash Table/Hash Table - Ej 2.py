
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def hash_function(self, key):
        h = 0
        for char in key:
            h += ord(char)
            # ord convierte código ASCII
        return h % self.MAX

    def add(self, key, value):
        h = self.hash_function(key)
        data = [(key,value)]
        if self.arr[h] == []:
            self.arr[h] = data
        else:
            self.arr[h].append((key, value))

    def print(self):
        print(self.arr)

    def getitem(self,key):
        h = self.hash_function(key)
        return self.arr[h]

hash = HashTable()
hash.add("Lunes", 320)
hash.print()
hash.add("senuL", 970)
hash.print()
hash.add("Santino", 100)
hash.add("onitnaS", 200)
hash.print()
hash.add("Franco", 900)
hash.print()