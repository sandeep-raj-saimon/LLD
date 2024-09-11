# Strategy design pattern is one of the behavioral design pattern.
# Strategy pattern is used when we have multiple algorithm for a specific task,
# and client decides the actual implementation to be used at runtime

from abc import ABC, abstractmethod

# The Strategy Interface
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass

# Concrete Strategy 1: No Discount
class NoDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price

# Concrete Strategy 2: Percentage Discount
class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, price):
        return price - (price * self.percentage / 100)

# Concrete Strategy 3: Fixed Amount Discount
class FixedDiscount(DiscountStrategy):
    def __init__(self, discount_amount):
        self.discount_amount = discount_amount

    def apply_discount(self, price):
        return price - self.discount_amount

# The Context Class (Product)
class Product:
    def __init__(self, name, price, discount_strategy: DiscountStrategy):
        self.name = name
        self.price = price
        self.discount_strategy = discount_strategy

    def get_price(self):
        return self.discount_strategy.apply_discount(self.price)

# Client code
if __name__ == "__main__":
    product = Product("Laptop", 1000, NoDiscount())
    print(f"Price of {product.name} with no discount: {product.get_price()}")

    product = Product("Laptop", 1000, PercentageDiscount(10))
    print(f"Price of {product.name} with 10% discount: {product.get_price()}")

    product = Product("Laptop", 1000, FixedDiscount(100))
    print(f"Price of {product.name} with $100 discount: {product.get_price()}")


# Benefits of Using Strategy Pattern:
# Open for Extension, Closed for Modification: To add a new discount strategy, we simply create a new strategy class without modifying the existing Product class.
# Encapsulation of Algorithms: Each discount calculation logic is encapsulated in its own class, following the single responsibility principle.
# Easier to Maintain: The code is cleaner and easier to extend, as each discount type is handled separately, and the client code is unaware of the discount calculation details.