class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price

    def get_info(self):
        print("Kniha", self.title, "má", self.pages, "stran a stojí", self.price, "Kč.")

    def discount(self, amount):
        self.price = self.price * (1 - amount / 100)
    
book = Book("Pýcha a předsudek", 200, 100)
book.get_info()

book.discount(10)
book.get_info()
