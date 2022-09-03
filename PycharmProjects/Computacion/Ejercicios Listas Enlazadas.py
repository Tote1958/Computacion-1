"""1) Eliminar primera aparicion value
2) Insertar despues de un value
3) Imprimir lista de atras-adelant
4) Invertir Lista"""

class Nodo:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Nodo(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("La lista esta vacia")
            return
        iterator = self.head
        str_list = ""
        while iterator:
            str_list += str(iterator.data) + "-->"
            iterator = iterator.next
        print(str_list)

    def size(self):
        if self.head is None:
            print("La lista esta vacia")
        str_list = ""
        counter = 0
        iterator = self.head

        while iterator:
            while iterator:
                str_list += str(iterator.data) + "-->"
                iterator = iterator.next
                counter = counter + 1
        return counter

    def insert_at(self, index, data):
        if index < 0 or index > self.size():
            raise Exception("Ingresaste un numero invalido")
        if index == 0:
            self.insert_at_beginning(data)
            return
        counter = 0
        iterator = self.head
        while iterator:
            if counter == index - 1:
                node = Nodo(data, iterator.next)
                iterator.next = node
                break

    def insert_at_end(self, data):
        index = self.size()
        counter = 0
        iterator = self.head
        while iterator:
            if counter == index - 1:
                node = Nodo(data, iterator.next)
                iterator.next = node
                break
            counter = counter + 1
            iterator = iterator.next

    def remove_at_first_value(self, value):
        iterator = self.head
        while iterator:
            if iterator.next.data == value:
                iterator.next = iterator.next.next
                break
            else:
                iterator = iterator.next
        return

    def insert_after_first_value(self, value, data):
        iterator = self.head
        while iterator:
            if iterator.data == value:
                node = Nodo(data, iterator.next)
                iterator.next = node
                break
            else:
                iterator = iterator.next

    def print_reverse_list(self):
        list = []
        iterator = self.head
        while iterator:
            list.append(iterator.data)
            iterator = iterator.next
        list.reverse()
        print(list)

    def reverse_list(self):
        list = []
        iterator = self.head
        while iterator:
            list.append(iterator.data)
            iterator = iterator.next
        self.head = None
        for i in range(len(list)):
            node = Nodo(list[i], self.head)
            self.head = node

ll = LinkedList()
ll.insert_at_beginning(23)
ll.insert_at_beginning(12)
ll.insert_at_beginning(34)
ll.insert_at_beginning(45)
ll.print()
ll.insert_at(1, 45)
ll.print()
ll.remove_at_first_value(12)
ll.print()
ll.insert_after_first_value(34, 56)
ll.print()
ll.print_reverse_list()
ll.reverse_list()
ll.print()