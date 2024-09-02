class Order:
    def __init__(self, items):
        self.items = items
        self.price = {
            'dosa': 100,
            'idli': 50
        }
    def calculateTotal(self):
        total = 0
        for item in self.items:
            total += self.price[item]
        return total

order = Order(['dosa'])
total = order.calculateTotal()

# in case we want to change the price, we need to make changes to the class
# this class has more than 1 responsibility, hence we should break it down to more simpler classes