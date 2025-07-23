# Create a class BankAccount with:

# A private attribute _balance

# A @property to get balance

# A @balance.setter to update balance (but reject negative values)

# class BankAccount:
#     def __init__(self,_balance):
#         self._balance = _balance
#     @property
#     def balance(self):
#         return f"the balance in your account is {self._balance}"
#     @balance.setter
#     def balance(self,amount):
#         if amount >= 0:
#             self._balance +=amount
#             print("the amount is updated")
#         else:
#             print("rejected")

#     def withdraw(self,amount):
#         if amount<0:
#             print(f"the amount must be greater than zero")
#         elif amount>self._balance:
#             print("insufficient balance")
#         else:
#             self._balance-=amount
#             print(f"withdraw amount is {amount}")
        
# ab = BankAccount(200)
# print(ab.balance)
# ab.balance = 45
# print(ab.balance)
# ab.withdraw(100)
# print(ab.balance)

#Area and diameter of a circle

class Circle:
    def __init__(self,radius):
        self._radius = radius
    @property
    def radius(self):
        return self._radius
    @property
    def area(self):
        return 3.14 * self._radius * self._radius
    @property
    def diameter(self):
        return f"{2 * self._radius:.2F}"
    @radius.setter
    def radius(self,rad1):
        self._radius = rad1
        print(f"the radius is updated to {rad1}")
c1 = Circle(5)
print(c1.radius)
print(c1.area)
print(c1.diameter)
c1.radius=6
print(c1.radius)
print(c1.area)
print(c1.diameter)
