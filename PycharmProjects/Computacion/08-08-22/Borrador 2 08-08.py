class Queue:
    def __init__(self):
        self.elements = []

    def push(self):
        element = input("Ingrese el elemento a ingresar en la cola: ")
        self.elements.append(element)

    def pop(self):
        try:
            return self.elements.pop(0)
        except IndexError:
            raise ValueError("La cola esta vacia")

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return self.elements == []
