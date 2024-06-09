"""
Definition:
A decorator is a callable object which takes function as a argument
and returns the modified function without modifying the original function...
SYNTAX:
def <decorator_name>(<taken_function_name>):
def wrapper(<taken_function_arguments>):
<Decoration Logic>
return wrapper

import time
def f1():
start = time.time()
print(f"function {f1.__name__} execution started")
for item in range(1000000):
print("India")
print("Python")
end = time.time()
print(f"function {f1.__name__}execution took {end-start} seconds")
def f2():
start = time.time()
print(f"function {f1.__name__} execution started")
for item in range(100000):
print(f"Current item is {item}")
end = time.time()
print(f"function {f2.__name__} execution took {end-start} seconds")
def f3():
start = time.time()
print(f"function {f3.__name__} execution started")
for item in range(500000):
pass
end = time.time()
print(f"function {f3.__name__} execution took {end-start} seconds")
f1()
f2()
f3()
"""
"""

import time
def get_fun_running_time(fun):

def wrapper(*args,**kwargs):
start = time.time()
print(f"function {fun.__name__} execution started")
fun() # Original function execution
end = time.time()
print(f"function {fun.__name__} execution took {end - start} seconds")
return wrapper
@get_fun_running_time
def f1():
for item in range(100000):
print("India")
print("Python")
@get_fun_running_time
def f2():
for item in range(10): # range(10) -> [0,1....9]
print("India")
print("Python")
@get_fun_running_time
def f3():
time.sleep(5)
# f1()
# f2()
f3()

def make_up(fun):
print("Make up Started")
def wrapper(*args ,**kwargs):
print(f"Person arrived..")
result = fun() # Original fun triggered
print(f"Make has been completed for {result} .. Next person please...")
return wrapper
@make_up
def person_name():
return "John Doe"

person_name()

# Database info after sign up
facebook = {"email": "john@gmail.com", "password": "Welcome@123"}
def login(func):
def wrapper(*args, **kwargs):
print(f"Function {func.__name__} being executed....")

result = func() # Original
# Logic to check valid user or not
if facebook["email"] == result["email"] and facebook["password"] == result["pa
return True # Valid user
else:
return False # InValid user
return wrapper
@login
def user1():
return {"email": "johndoe@gmail.com", "password": "Welcome@123"}
res = user1()
if res == True:
print("User is successfully authenticated with valid credentials")
else:
print("Invalid EMail/Password.. Try again!")

# Write a decorator to split a string
def split_str(fun):
def wrapper(*args,**kwars):
original_str = fun()
res = original_str.split(",")
return " ".join(res)
return wrapper
@split_str
def get_str():
return "Hello,Everyone,Welcome,to,Python"
print(get_str())
"""
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


#split string

def string_splitter(func):
    def wrapper(string):
        words = string.split()
        return func(words)
    return wrapper

@string_splitter
def print_words(words):
    for word in words:
        print(word)

print_words("Hello world! This is a string.")


#data base entry
def database_entry(func):
    def wrapper(username):
        print(f"Database entry created for user: {username}")
        return func(username)
    return wrapper

def logging_info(func):
    def wrapper(username):
        print(f"User {username} signed up successfully")
        return func(username)
    return wrapper

@database_entry
@logging_info
def sign_up(username):
    pass

sign_up("Alice")

#user database


user_database = {
    'alice@example.com': 'password123',
    'bob@example.com': 'bob_password',
}

def authenticate(func):
    def wrapper(email, password):
        if email in user_database and user_database[email] == password:
            print(f"User {email} logged in successfully")
            return func(email, password)
        else:
            print("Invalid email or password")
    return wrapper

@authenticate
def login(email, password):
    # Placeholder for additional login logic
    pass

# Example usage
login('alice@example.com', 'password123')
login('alice@example.com', 'wrong_password')
login('charlie@example.com', 'password123')