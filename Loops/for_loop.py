# for i in range(1,11):
#     print("56 x", i ,"=", 56 * i)
# Escape sequences in Python allow special characters to be represented within strings. Your task is to write a Python program that prints the below text exactly as shown:

# Hello, Python Learner
# I am "good"

# print("Hello\\, Python \tLearner\nI am \"good\'")

season = input("enter the season:-")
crops = ["turmaric","cotton","soya","corn","vegetables","chillis"]
for crop in crops:
    if season == "rainy":
        print(f"you can sow {crops[0]}")
        break
    elif season == "winter":
        print(f"you can prefer {crops[1]}\\{crops[2]} ")
        break
    elif season == "spring":
        print(f"you can prefer {crops[3]}\\{crops[5]}")
        break
    elif season == "summer":
        print(f"the only choice you have is {crops[4]}")
        break
    else:
        print("This is the worst years as there are no rains")
        break