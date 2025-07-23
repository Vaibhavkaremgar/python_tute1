# BankAccount Class
# Create a BankAccount class with:

# Attributes: account_holder, balance

# Methods:

# deposit(amount) — add money

# withdraw(amount) — deduct money if enough balance

# display_balance() — show balance

#code1

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


#code2

class BankAccount:
    def __init__(self,account_holder, balance,branch):
        self.account_holder = account_holder
        self.balance = balance
        self.branch = branch
    def add_money(self,amount):
        #if self.branch == "kini":
            self.balance+=amount
            print(f"the deposited amount is {amount} and the updated balance is {self.balance}")
        #else:
            #print(f"please visit your home branch as this is {self.branch} branch")
    def withdraw_money(self,amount):
        #if self.branch == "kini":
            if self.balance>= amount:
                self.balance-=amount
                print(f"debited amount is {amount} and the updated balance is {self.balance}")
            else:
                print(f"your acc balance is {self.balance}, so you can't withdraw the amount")
        #else:
            #print(f"please visit your home branch")
    def get_balance(self):
        print(f"the balance in your account is {self.balance}")

allowed_branches = ["kini","paki","palaj","nanda","maldhary"]
acc1 = BankAccount("vaibhav",300,"bhainsa")
if acc1.branch in allowed_branches:
    acc1.add_money(int(input("enter the credit amount:-")))
    acc1.withdraw_money(int(input("enter the withdrawal amount:-")))
    acc1.get_balance()
else:
     print(f"pls visit your home branch your home branch is {acc1.branch}")
print(f"Thank you for visiting sbi bank ,{acc1.branch}!! pls visit us again")

