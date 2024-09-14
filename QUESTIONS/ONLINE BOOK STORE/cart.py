from user import User
from cart_item import CartItem
from book import Book
from book_item import BookItem
from user_type import UserType
from typing import List
class Cart:
    def __init__(self, user: User):
        self.user = user
        self.cart_items: List[CartItem] = [] # at the beginning the cart is going to be empty
        self.total_amount = self.get_total()
    
    def get_total(self):
        total = 0
        for cart_item in self.cart_items:
            total += cart_item.get_price()
        return total
    
    def add_to_cart(self, cart_items: CartItem):
        self.cart_items.append(cart_items)

    def remove_from_cart(self, cart_items: CartItem):
        self.cart_items.remove(cart_items)
        
    
# u = User(1, UserType.USER)
# b = Book(1, 'test', 20, 100, 'sandeep', 'thriller')
# b_i = BookItem(b, 1)
# c_i = CartItem(u, b_i)
# c = Cart(u)
# c.add_to_cart(c_i)
# print(c.get_total())
# c.remove_from_cart(c_i)
# print(c.get_total())