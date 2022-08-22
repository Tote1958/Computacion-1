class Stack:
    def __init__(self):
        self.elements =[]

    def push(self):
        element = input("Ingrese el elemento a ingresar en la pila: ")
        self.elements.append(element)

    def pop(self):
        try:
            return self.elements.pop()
        except IndexError:
            raise ValueError("La pila esta vacia")

    def peek(self):
        return self.elements[-1]

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return self.elements == []

pila = Stack()
pila.push()
print(pila.peek())
