# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print(f"My name is {self.name} and I am {self.age} years old.")

# # Creating an object
# p1 = Person("Vaibhav", 28)
# p1.introduce()
# Create a Student Class
# Attributes: name, roll_no, marks

# Method: display_info() → prints the student details

# class Student:
#     def __init__(self,name,roll_no,marks):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks
#     def display_info(self):
#         print(f"my name is {self.name} and roll_no is {self.roll_no} and i got {self.marks} marks")
# s1 = Student("vaibhav",489,99)
# s1.display_info()

# Create a Circle Class
# Attribute: radius

# Method: get_area() → returns area of the circle (πr²)

# Method: get_circumference() → returns circumference (2πr)
# import math
# class circle:
#     def __init__(self,radius):
#         self.radius = radius
#     def get_area(self):
#         return math.pi*self.radius**2
#     def get_circumference(self):
#         return 2*math.pi*self.radius
# c1 = circle(10)
# print(c1.get_area())
# print(c1.get_circumference())

# Create a class with methods:

# add(a, b)

# subtract(a, b)

# multiply(a, b)

# divide(a, b) → (handle division by zero gracefully)
# class Calculator:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def addition(self):
#         print(f"the sum of the 2 num is {self.a + self.b}")
#     def subtract(self):
#         print(f"the diff of 2 num is {self.a - self.b}")
#     def multiply(self):
#         print(f"the prod of 2 num is {self.a * self.b}")
#     def division(self):
#         if self.b == 0:
#             print("error becoz zero division is not allowed")
#         else:
#             print(f"the div of 2 num is {self.a / self.b:.2f}")
# c1 = Calculator(5,0)
# c1.addition()
# c1.subtract()
# c1.division()
# c1.multiply()

# Bank System
# Class: BankAccount

# Attributes: account_holder, balance

# Methods: deposit(amount), withdraw(amount), get_balance()

# Restrict withdrawal if balance is too low


# class BankAccount:
#     def __init__(self,account_holder, balance,branch):
#         self.account_holder = account_holder
#         self.balance = balance
#         self.branch = branch
#     def add_money(self,amount):
#         #if self.branch == "kini":
#             self.balance+=amount
#             print(f"the deposited amount is {amount} and the updated balance is {self.balance}")
#         #else:
#             #print(f"please visit your home branch as this is {self.branch} branch")
#     def withdraw_money(self,amount):
#         #if self.branch == "kini":
#             if self.balance>= amount:
#                 self.balance-=amount
#                 print(f"debited amount is {amount} and the updated balance is {self.balance}")
#             else:
#                 print(f"your acc balance is {self.balance}, so you can't withdraw the amount")
#         #else:
#             #print(f"please visit your home branch")
#     def get_balance(self):
#         print(f"the balance in your account is {self.balance}")

# allowed_branches = ["kini","paki","palaj","nanda","maldhary"]
# acc1 = BankAccount("vaibhav",300,"bhainsa")
# if acc1.branch in allowed_branches:
#     acc1.add_money(int(input("enter the credit amount:-")))
#     acc1.withdraw_money(int(input("enter the withdrawal amount:-")))
#     acc1.get_balance()
# else:
#      print(f"pls visit your home branch your home branch is {acc1.branch}")
# print(f"Thank you for visiting sbi bank ,{acc1.branch}!! pls visit us again")

# Base class: Vehicle
#   - Attribute: max_speed
#   - Method: show_info()

# Subclass: Car
#   - Attributes: brand, model
#   - Method: show_info() → overrides parent method and shows all info

# Create an object of Car and call show_info()

class Vehicle:
    def __init__(self,max_speed):
        self.max_speed = max_speed
class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(max_speed=300)
        self.model = model
        self.brand = brand
        self.odometer = 0
        self.engine_on = False
        self.speed = 0
    def show_info(self):
        return f"the max speed of the {self.brand} car is {self.max_speed} and the model is {self.model}"
    def start_engine(self):
        if not self.engine_on:
            self.engine_on = True
            print(f"the {self.brand} car of {self.model} model's engine is on")
        else:
            print("engine is already running")
    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            self.speed = 0
            print("the engine is stopped")
        else:
            print("the engine is already stopped")
    def accelerate(self,speed_increase,duration):
        if not self.engine_on:
            print("start the engine first")
            return
        
        self.speed+=speed_increase
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        distance = self.speed * duration
        self.odometer += distance
        print(f"the vehicle is accelareted with {self.speed}km/hr")
v2 = Car("baleno", "sigma")
print(v2.show_info())
v2.start_engine()
v2.accelerate(speed_increase=140,duration=2)
v2.stop_engine()

# Add attributes in __init__():

# self.odometer = 0

# self.engine_on = False

# self.speed = 0

# Create method start_engine(self):

# Set self.engine_on = True

# Print: "Engine started."

# Create method stop_engine(self):

# Set self.engine_on = False

# Set self.speed = 0

# Print: "Engine stopped."

# Create method accelerate(self, speed, duration):

# If engine_on == False: print "Start the engine first!"

# Else:

# Set self.speed = min(speed, self.max_speed)

# Calculate distance = self.speed * duration

# Add distance to odometer


    