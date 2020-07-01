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

print('')


# Staticmethods and classmethods

class ClassTest:
    # instance methods are basic methods > used for most things
    def instance_method(self):
        print(f'Called instance_method of {self}')

    # def __repr__(self):
    #     return f'<ClassTest method repr>'

    # class methods are used as factories
    @classmethod
    # cls is the class itself
    def class_method(cls):
        print(f'Called class_method of {cls}')

    # static methods used to place a method in a class
    # Mostly just for code organization
    @staticmethod
    def static_method():
        print('Called static_method')


ClassTest.class_method()
test = ClassTest()
test2 = ClassTest()

test.instance_method()
test2.instance_method()
ClassTest.instance_method(test)

ClassTest.static_method()

print('')


class Book:
    # limits values for arguments
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f'<Book: {self.name}, {self.book_type}, weighs {self.weight}g>'

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)

    @classmethod 
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


book1 = Book.hardcover('Chamber of Secrets', 1500)
book2 = Book.paperback('The Hobbit', 1200)

print(book1)
print(book2)


# Exercise 7

class Store2:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, 
        # plus " - franchise"
        return cls(store.name + ' - franchise')

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return f'{store.name}, total stock price: {int(store.stock_price())}'

storea = Store2('Test')
storeb = Store2('Sean Mart')
storeb.add_item('Apple', 15)
storeb.add_item('Bannanna', 20)

print(Store2.franchise(storea).name)
print(Store2.store_details(storeb))

# Store.store_details(store)
