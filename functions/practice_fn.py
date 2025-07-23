# def fun(a,b,c=5):
#     return a + b + c
# print(fun(a = 5,b = 2))

# def student(name,age,marks):
#     return f"the name of the student who got {marks} marks is {name} and he is {age} years old"
# print(student(name="vaibhav",age=25,marks=99))
# def doc(a,b):
#     """returns the multiplication of the numbers"""
#     return a * b 
# print(doc.__doc__)
# print(doc(5,6))

# Write a simple function greet that prints "Hello, welcome!"
# Then call it.

# def greet():
#     print("hello,Welcome!")
# greet()

# Write a function greet_person that takes one parameter name and prints:
# "Hello, <name>! Welcome!"
# def greet_person(name):
#     return f"Hello , {name}! Welcome!"
# print(greet_person("vaibhav"))
# Write a function add_numbers that takes two numbers, adds them, and returns the sum.

# def add_numbers(a,b=5):
#     return a + b 
# print(add_numbers(4))
# Write a function sum_all that accepts any number of numbers and returns their sum.
# def sum_all(*args):
#     """Accepts any number of numeric arguments and returns their sum."""
#     return sum(args)
# print(sum_all(1,2,3,4,5))

#*kwargs
# def print_details(**kwargs):
    # for key, value in kwargs.items():
        # print(f"{key} : {value}")

# print_details(name="Vaibhav", age=25, city="Pune",state="Maharashtra",country="India")

# Write a function greet_user that takes name and msg (default to "Good morning").
# If msg isn’t passed, it should greet with "Good morning".

# def greet_user(name,msg="Good morning"):
#     return f"{msg}, {name}"
# print(greet_user("vaibhav"))
# print(greet_user("vaibhav", "Hi"))
# Write a function that multiplies all numbers passed to it
# Example: multiply_all(2, 3, 4) --> 24
# def Multiply_all(*args):
#     result = 1
#     for num in args:
#         result*=num
#     return result
# print(Multiply_all(2,3,4))
# Write a function max_num that accepts any number of numbers using *args and returns the largest number.

# def max_num(*args):
#     return max(args)
# print(max_num(2,3,8,9))

# Write a function print_pet_info that accepts keyword arguments for name and animal and prints:
# "<name> is a <animal>."

# def print_pet_info(**kwargs):
#     for name,animal in kwargs.items():
#         return f"{name} is a {animal}"
# print(print_pet_info(name="brownie", animal = "dog"))

# Write a function max_num that takes any number of numbers and returns the largest one.
# def max_num(*args):
#     return max(args)
# print(max_num(2,3,8,9))
# count_odds(*args) — count how many numbers are odd!
# Want a hint again or ready to write
# def count_odds(*args):
#     result = 0
#     for num in args:
#         if num%2 != 0:
#             result+=1
#     return result
# print(count_odds(1,2,3,4,5,6,7,8,9))

def kwar(*args,**kwargs):
    for name,gender in kwargs.items():
        return f"{name} is a {gender}"
print(kwar(name="vaibahv", gender="male"))
print("items:", *args)


