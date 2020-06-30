def hello(name):
    print(f'Heeyyy {name}')


hello('Sean ' * 5)

# Complete the function by making sure it returns 42. .
def return_42():
    # Complete function here
    return 42  # 'pass' just means "do nothing". Make sure to delete this!

# Create a function below, called my_function, that takes two arguments and returns the result of its two arguments multiplied together.

def my_function(x, y):
    return x * y
    
print(my_function(5, 10))


# Unpacking arguments
def show(*args):
    print (args[1])

show(1, 2, 3)

def add(x, y):
    return x + y

nums = [3, 5]
print(add(*nums))

nums_dict = {'x': 7, 'y': 9}
print(add(**nums_dict))

# Unpacking keyword arguments
def named(**kwargs):
    print(kwargs)

named(name="Sean", age=36)

def named2(name, age):
    print(name, age)

details = {'name': 'Caitlin', 'age': 33}

named2(**details)


