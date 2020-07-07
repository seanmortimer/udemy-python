class Checkout:
    class Discount:
        def __init__(self, quantity, price):
            self.quantity = quantity
            self.price = price


    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}
        self.total = 0
    
    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item not in self.prices:
            raise Exception("Item is missing price")
        if item in self.items:
           self.items[item] += 1
        else:
           self.items[item] = 1

    def addDiscount(self, item, quantity, price):
        discount = self.Discount(quantity, price)
        self.discounts[item] = discount
        
    def totalItems(self):
        total = 0
        for (item, cnt) in self.items.items():
            total += self.calculateItemTotal(item, cnt)
        return total
        
    def calculateItemTotal(self, item, count):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if count >= discount.quantity:
                total += self.calcItemDiscount(item, count, discount)
            else:        
                total+= self.prices[item] * count
        else:        
            total += self.prices[item] * count
        return total

    def calcItemDiscount(self, item, count, discount):
        total = 0
        quantity = count / discount.quantity
        total += quantity * discount.price
        remain = count % discount.quantity
        total += remain * self.prices[item]
        return total
