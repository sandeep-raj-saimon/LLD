from book_item import BookItem
from book import Book
class CartItem:
    def __init__(self, user, book_item: BookItem):
        self.user = user
        self.book_item = book_item
        self.book_item.book.reduce_quantity(self.book_item.get_quantity())

    def get_price(self):
        return self.book_item.get_price() * self.book_item.get_quantity()
# id, name, quantity, price, author, genres
# b = Book(1, 'test', 20, 100, 'sandeep', 'thriller')
# b_i = BookItem(b, 1)
# c_i = CartItem(u, b_i)