import random
import balance

class Store:
    #^ simulates buying items to work with transaction dict
    def __init__(self):
        self.items = ['pants', 'toy', 'phone', 'bowl', 'pot']
        self.purchases = balance.Transactions()

    def display_item(self):
        item = self.items[random.randint(0, 4)]
        price = random.randint(5, 25)

        return item, price

    def purchase(self, item, price):
        self.purchases['online'] = price
        


        