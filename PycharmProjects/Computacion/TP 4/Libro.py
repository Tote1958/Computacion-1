class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def viewBook(self):
        print("Titulo:", self.title)
        print("Autor:", self.author)
        print("Precio:", self.price)

