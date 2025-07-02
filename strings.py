# a = 'vaibhav'
# b = " reddy"
# c = '''    He came from a village located near bhainsa    '''
# age = 25

# print(a[0])
# print(b[-3])
# print(c[-10])

# print(a[1:3])
# print(b[:4])
# print(c[-5:-1])
# print(c[13::])

# print(a.upper())
# print(b.lower())
# print(c.strip())
# print(c.replace("came", "is").strip().split())
# print(c.split())

# print("my name is {} and my age is {}".format ((a+ b),age))
# print(f"my name is {a} and i am {age} years old")

# for i in range (97,110):
#     print(chr(i),end = " ")

# for i in 'a b c d':
#     print(ord(i),end = "")

# text = "apple,banana,guava"

# print(text.split())
# print(",".join(['apple,banana,guava']))

# print(ord())

# You are given the following initial code:



# greeting = "Hi"
# language = "Java"
# status = "bad"
 
# print(f"{greeting}, Python Learner")
# print(f"I am \"{status}\"")
# Change the values of the variables so that the program prints exactly:

# Hello, Python Learner
# I am "good"

# greeting = "Hello"
# language = "Python"
# status = "good"

# print(f"{greeting}, {language} Learner\nI am \"{status}\"")

# main = ("a","e","i","o","u")
# letter = "vaibhav"

# for i in letter:
#     if i in main:
#         print(i)
# print(letter[::-1])
# print(letter[2::])

# name = "vaibhav"
# result = []
# for i in name:
#     result.append(i)
# print(result)

# def myfunc(args):
#     result = ''
#     for i in enumerate(args) :
#         if i % 2 == 0:
#             result += args[i].lower()
#         else:
#             result += args[i].upper()
#     return result
# print(myfunc("VaIbHaV123 RedDy"))
# Create a list of numbers:

words = ['banana', 'apple', 'kiwi', 'pineapple', 'grape']

for word in words:
    print(word,len(word))