# this class is kind of metadata
class Book:
    def __init__(self, id, name, quantity, price, author, genres):
        self.book_id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.author = author
        self.genres = genres

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author
    
    def get_genres(self):
        return [(i.type) for i in self.genres]
    
    def get_quantity(self):
        return self.quantity
    
    def get_price(self):
        return self.price
    
    def reduce_quantity(self, quantity = 1):
        if (self.quantity - quantity >= 0):
            self.quantity -= quantity
        else:
            raise Exception('Does not have required quantity')
        
    
