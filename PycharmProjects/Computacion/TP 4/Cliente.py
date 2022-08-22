class Client:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def viewClient(self):
        print("Nombre:", self.name)
        print("Edad:", self.age)
        print("Direccion:", self.address)

