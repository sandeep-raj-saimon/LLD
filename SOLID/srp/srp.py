class Price:
    def __init__(self):
        self.prices = None
    
    def getPrices(self):
        return self.prices
    
    def setPrices(self, prices):
        self.prices = prices

class Order:
    def __init__(self, items, price):
        self.items = items
        self.prices = price.getPrices()
    def calculateTotal(self):
        total = 0
        for item in self.items:
            total += self.prices[item]
        return total

price = Price()
price.setPrices(({ 'dosa': 110, 'idli': 80 }))
order = Order(['dosa'], price)
total = order.calculateTotal()
print(total)