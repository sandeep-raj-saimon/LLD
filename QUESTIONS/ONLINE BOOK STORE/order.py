from order_status import OrderStatus
from cart import Cart
class Order:
    def __init__(self, user, cart: Cart):
        self.cart = cart
        self.user = user
        self.total = self.get_total()
        self.status = OrderStatus.ACCEPTED

    def get_total(self):
        return self.cart.get_total()
    
    def get_status(self):
        return self.status
    
