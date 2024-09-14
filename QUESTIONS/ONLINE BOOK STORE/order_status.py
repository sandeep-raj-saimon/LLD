from enum import Enum
class OrderStatus(Enum):
    ACCEPTED = 1
    SHIPPED = 2
    OUT_FOR_DELIVERY = 3
    DELIVERED = 4