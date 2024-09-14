class A:
    def __init__(self, a) -> None:
        self.a = a

    def get_a(self):
        return self.a

class B(A):
    def __init__(self, b):
        self.b = b
    
    def get_a(self):
        return super().get_a()
    
a = A(1)
b = B(2)
print(b.get_a())
