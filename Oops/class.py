# Write a Car class with:

# Attributes: brand, model, year

# Method: description() which prints the car’s details

class Car():
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def car_features(self):
        print(f"The {self.brand} car manufactured in {self.year} is a {self.model}")
car1 = Car("baleno","sigma varient",2020)
car1.car_features()
car2 = Car("hundai","mid varient",2023)
car2.car_features()

# Practice Example 1: Book Class
# Create a Book class with:

# Attributes: title, author, pages

# Method: book_info() that prints the book details
class Book():
    def __init__(self,title,author,pages,price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
    def book_details(self):
        print(f"The {self.title} book written by {self.author} has {self.pages} pages that costs {self.price}")

Book1 = Book("na savu nen sastha","koushik",420,360)
Book1.book_details()

# ✅ Practice Example 2: Student Class
# Create a Student class with:

# Attributes: name, roll_number, marks

# Method: display() that prints student info

# Method: is_passed() — returns True if marks > 40, else False



class Student():
    def __init__(self,name,roll_number,marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display(self):
        print(f"{self.name} with {self.roll_number} roll_number got {self.marks} marks")

    def is_passed(self):
        if self.marks > 40:
            return True
        else:
            return False
Student1 = Student("Vaibhav",489,74)
Student1.display()
print(Student1.is_passed())


# ✅ Practice Example 3: BankAccount Class
# Create a BankAccount class with:

# Attributes: account_holder, balance

# Methods:

# deposit(amount) — add money

# withdraw(amount) — deduct money if enough balance

# display_balance() — show balance

class BankAccount():
    def __init__(self,account_holder,balance,branch):
        self.account_holder = account_holder
        self.balance = balance
        self.branch = branch
    def add_money(self,amount):
        self.balance+=amount
        print(f"Deposited {amount}. new balance is {self.balance}")
    def withdraw_money(self,amount):
        if self.balance >= amount:
            self.balance-=amount
            print(f"You have withdrawn {amount} and your updated balance is {self.balance}")
        else:
            print(f"you have {self.balance}, so you are not allowed to withdraw")
    def display_balance(self):
        print(f"your current balance is {self.balance}")
Account1 = BankAccount("vaibhav", 101, "kini")
Account1.add_money(int(input("enter the amount")))
Account1.withdraw_money(int(input("enter the amount")))
Account1.display_balance()