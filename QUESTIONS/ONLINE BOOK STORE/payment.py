from payment_mode import PaymentMode
from order import Order
from payment_status import PaymentStatus

class Payment:
    def __init__(self, order: Order) -> None:
        self.order = order
        self.amount = self.order.get_total()
        self.mode_of_payment = PaymentMode.CASH
        self.status = PaymentStatus.PENDING

    def get_order(self):
        return self.order
    
    def get_amount(self):
        return self.amount