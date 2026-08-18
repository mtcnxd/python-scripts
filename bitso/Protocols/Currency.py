from .AbstractCurrency import AbstractCurrency

class Currency (AbstractCurrency):
    def __init__(self):
        self.price = 0
        self.book = 0

    def set_price(self, price: str): 
        self.price = price
        return self
    
    def set_book(self, book: str): 
        self.book = book
        return self

    def __str__(self):
        return f"Name: {self.book} - Value: {self.price}"