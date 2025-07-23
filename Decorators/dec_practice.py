# Create a decorator called welcome_decorator that:

# Prints "Welcome!" before the actual function runs

# Prints "Have a nice day!" after the function runs
# def welcome_decorator(func):
#     def wrapper():
#         print("welcome!")
#         func()
#         print("have a nice day!")
#     return wrapper
# @welcome_decorator
# def say_something():
#     print("This is your copilot")
# say_something()

# Create a decorator greet_decorator that:

# Prints "Greeting user..." before the function

# Passes the name to the function as an argument

# def greet_decorator(func):
#     def wrapper(a):
#         print("Greeting user...")
#         func(a)
#     return wrapper
# @greet_decorator
# def greet(name):
#     print(f"the name of the person is {name}")
# greet("vaibhav")

# Create a decorator called timer_decorator that:

# Measures how long the function takes to run

# Prints the execution time in seconds

# import time
# def timer_decorator(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f"function took {end - start:.2F} seconds to execute")
#     return wrapper
# @timer_decorator
# def time_taken():
#     time.sleep(2)
#     print("task is done")
# time_taken()

# You need to create a decorator check_access that:

# Checks if a user has admin rights (is_admin = True)

# If True, allow the function to run

# If False, print "Access Denied!" and don’t run the function

# is_admin = False

# def check_access(func):
#     def wrapper():
#         if is_admin:
#             func()
#         else:
#             print("access denied")
#     return wrapper
# @check_access
# def delete_user():
#     print("removed")
# delete_user()

# import pygame
# pygame.init()
# print("Pygame installed and working!")
# pygame.quit()
# Write a decorator called log_decorator that prints the function name before it's called.

# python
# Copy
# Edit
# @log_decorator
# def multiply(a, b):
#     return a * b

# multiply(3, 4)
# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling function: {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper

# @log_decorator
# def multiply(a, b):
#     return a * b

# print(multiply(3, 4))
# Create a decorator named debug that:

# Prints the arguments passed to a function

# Then executes the function

# Finally, returns the result

# def debug(func):
#     def wrapper(*args,**kwargs):
#         print(f"arguments of the function: {func.__name__,args}")
#         return func(*args, **kwargs)
#     return wrapper
# @debug
# def addition(a,b):
#     return a + b
# print(addition(3,4))
