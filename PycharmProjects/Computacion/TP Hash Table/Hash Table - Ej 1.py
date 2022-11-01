
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def hash_function(self,key):
        h = 0
        for char in key:
            h += ord(char)
            # ord convierte código ASCII
        return h % self.MAX

    def add(self,key,value):
        h = self.hash_function(key)
        self.arr[h] = value

    def print(self):
        print(self.arr)

    def getitem(self,key):
        h = self.hash_function(key)
        return self.arr[h]


hash = HashTable()
print(hash.hash_function("Lunes"))
hash.print()
print(hash.add("Lunes",320))
hash.print()
print(hash.add("Santino",400))
hash.print()
print(hash.add("senuL",970))
hash.print()
print(hash.getitem("Santino"))
