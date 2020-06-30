class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # prints this string instead of the literal object
    def __str__(self):
        return f'Person {self.name}, {self.age} years old'

    # prints the object, <> are formatting to represent an object
    def __repr__(self):
        return f'<Person( {self.name}, {self.age} years old)>'


bob = Person('Sean', 36)

print(bob)

# Exercise 6
class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []
    
    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        item = {'name': name, 'price': price}
        self.items.append(item)

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        # total = 0
        # for item in self.items:
        #     total += item['price']
        # return total
        
        # The better way: (list comprehension)
        return sum(item['price'] for item in self.items)
    
store = Store('Sean')

store.add_item('Apple', 10)
store.add_item('Banana', 20)

print(store.stock_price())

    