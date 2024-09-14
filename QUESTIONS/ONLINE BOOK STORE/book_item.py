from book import Book
class BookItem(Book):
    def __init__(self, book: Book, quantity):
        self.book = book
        self.quantity = quantity

    def get_price(self):
        return self.book.get_price()
    
    def get_quantity(self):
        return self.quantity
    
    
