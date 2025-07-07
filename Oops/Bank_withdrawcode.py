# BankAccount Class
# Create a BankAccount class with:

# Attributes: account_holder, balance

# Methods:

# deposit(amount) — add money

# withdraw(amount) — deduct money if enough balance

# display_balance() — show balance

class BankAccount():#Create a BankAccount class 
    def __init__(self,account_holder,balance,branch):# Attributes: account_holder, balance
        self.account_holder = account_holder
        self.balance = balance
        self.branch = branch
    def add_money(self,amount):# deposit(amount) — add money
        self.balance+=amount
        print(f"Deposited {amount}. new balance is {self.balance}")
    def withdraw_money(self,amount):# withdraw(amount) — deduct money if enough balance
        if self.balance >= amount:
            self.balance-=amount
            print(f"You have withdrawn {amount} and your updated balance is {self.balance}")
        else:
            print(f"you have {self.balance}, so you are not allowed to withdraw")
    def display_balance(self):# display_balance() — show balance
        print(f"your current balance is {self.balance}")
Account1 = BankAccount("vaibhav", 101, "kini")
Account1.add_money(int(input("enter the amount")))
Account1.withdraw_money(int(input("enter the amount")))
Account1.display_balance()

