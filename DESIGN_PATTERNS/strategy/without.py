class Product:
    def __init__(self, name, price, discount_type=None, discount_value=0):
        self.name = name
        self.price = price
        self.discount_type = discount_type
        self.discount_value = discount_value

    def get_price(self):
        if self.discount_type == 'none':
            return self.price
        elif self.discount_type == 'percentage':
            return self.price - (self.price * self.discount_value / 100)
        elif self.discount_type == 'fixed':
            return self.price - self.discount_value
        else:
            return self.price

# Client code
if __name__ == "__main__":
    product = Product("Laptop", 1000, 'none')
    print(f"Price of {product.name} with no discount: {product.get_price()}")

    product = Product("Laptop", 1000, 'percentage', 10)
    print(f"Price of {product.name} with 10% discount: {product.get_price()}")

    product = Product("Laptop", 1000, 'fixed', 100)
    print(f"Price of {product.name} with $100 discount: {product.get_price()}")
