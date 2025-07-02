# def total_products(a,b,c=5):# default arguments and parameters
#     return a + b + c 
# result = total_products(4,6,7)
# print(result)

# def marriage(groom,bride): # keyword arguments
#     print(f"{groom} and {bride} are getting married")
# marriage(groom="gopi", bride="ruchita")


# square = lambda x: x * x
# print(square(5))

# tip = lambda bill: bill * 0.10
# print(tip(500))

# def fib(n): 
#     if (n == 0  or n == 1):
#         return n
#     return fib(n-2) + fib(n-1)
# print(fib(50))

# def factorial(n):
#     if (n == 0 or n == 1):
#         return 1
#     return n * factorial(n-1)
# print(factorial(0))


# even = []
# for i in range (1,273):
#     if (i == 0 or i == 1):
#         False
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         pass
# print("all the even numbers are:-", even)


# prime = []
# def prime_num(n):
#     if n<=1:
#         return False
#     for i in range (2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# for num in range(1,238):
#     if prime_num(num):
#         prime.append(num)
# print("the prime numbers are:-",prime)

def vowels(word):
    vowel = ("a","e","i","o","u")
    for i in word:
        if i in vowel:
            print(f"the letter {i} is a vowel")
        else:
            print(f"the letter {i} is not a vowel")
vowels("vaibhav")