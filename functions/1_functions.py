# def total_products(a,b,c=5):
#     return a + b + c 
# result = total_products(4,6,7)
# print(result)

# def marriage(groom,bride):
#     print(f"{groom} and {bride} are getting married")
# marriage(groom="gopi", bride="ruchita")

def fib(n):
    if (n == 0  or n == 1):
        return n
    return fib(n-2) + fib(n-1)
print(fib(50))
