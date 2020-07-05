# First class functions
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by 0.")
            
    return dividend / divisor

def multiply(x: int, y:int):
    return x * y

def calculate(*values, operator):
    return operator(*values)

result = calculate(20, 4, operator=divide)
result2 = calculate(20, 4, operator=multiply)


# Decorators and 'at' syntax
import functools

def get_admin_pass():
    return "1234"

def make_secure(func):
    @functools.wraps(func)
    # def secure_fn(): <-- with no arguments
    def secure_fn(*args, **kwargs):
        if user1["access_level"] == "admin":
           return func(*args, **kwargs)
        
    return secure_fn
    
    
user1 = {"username": "jose", "access_level": "guest"}
user2 = {"username": "sean", "access_level": "admin"} 
user3 = {"username": "babazel", "access_level": "admin"}
user4 = {"username": "brian", "access_level": "user"}
# user3 = {"username": "babazel", "access_level": "admin"}

get_admin_pass = make_secure(get_admin_pass)
print(get_admin_pass())

# using decorators
def make_secure2(func):
    @functools.wraps(func)
    # def secure_fn(): <-- with no arguments
    def secure_fn(*args, **kwargs):
        u = args[0]
        # print(u)
        if u["access_level"] == "admin":
           return func(*args, **kwargs)
        else:
            return f"{u['username']} does not have admin rights."

    return secure_fn


@make_secure2
def get_pass(user):
    if user["username"] == "sean":
        return "Admin password is '1234'"
    else:
        return "I don't know you!"

print(get_pass(user1))
print(get_pass(user2))
print(get_pass(user3))


# Using parameters with the decorator
def make_secure3(access_level):
    def decorator(func):
        @functools.wraps(func)
        # def secure_fn(): <-- with no arguments
        def secure_fn(*args, **kwargs):
            # u = args[0]
            # print("secure_fn: ", u)
            if user1["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"{user1['username']} does not have {access_level} rights."

        return secure_fn

    return decorator
    

@make_secure3("admin")
def get_admin_pass3():
    return "admin: 1234"

@make_secure3("user")
def get_dash_pass():
    return "user: user_pass"

print(get_admin_pass3())
print(get_dash_pass())
print(get_dash_pass())
print(get_dash_pass())

