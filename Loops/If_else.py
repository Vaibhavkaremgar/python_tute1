# #Write an if-else block to check if a number is even or odd.
# number =int(input("enter a number:-"))

# if number % 2 == 0:
#     print("the number is even")
# else:
#     print("the number is odd")
# #Write a match-case block for day = 1 or 2 — print Monday, Tuesday, or Other day.

# day = int(input("enter the day number:-"))

# match day:
#     case 1:
#         print("monday")
#     case 2:
#         print("tuesday")
#     case _:
#         print("some other day")

# # Print numbers 1 to 5 using a for loop.
# for i in range(1,6):
#     print(i)

# # Print numbers 1 to 5 using a while loop.
# count = 1

# while count<=5:
#     print(count)
#     count+=1

# #Use a for loop to print numbers 1 to 10, but stop the loop when the number is 5

# for i in range (1,11):
#     if i ==5:
#         break
#     else:
#         print(i)

# for i in range (10,20):
#     if i == 11:
#         continue
#     else:
#         print(i)
# for i in range(1,6):
#     if i ==2:
#         pass
#     else:
#         print(i)

## Ask the user how many subjects they have, then take marks for each subject, add them up, and print the total marks and average
# num_of_sub = int(input("enter the number of subjects"))
# total_marks = 0
# for sub in range(1,num_of_sub+1):
#     marks = int(input("enter the marks of the sub:-"))
#     total_marks+=marks
# print(total_marks)
# print(total_marks/num_of_sub)

# #Keep asking the user for a password until they type "python123".
## Use a while loop!
# while True:
#     password = input("enter the password:-")
#     if password=="python123":
#         print("access granted")
#         break
#     else:
#         print("access denied, reenter the password")

# Loop through [5, 10, -3, 7, -1] — print each number, stop the loop when you find the first negative (use break).

# Numbers = [5, 10, -3, 7, -1]
# for number in Numbers:
#         if number<0:
#               break
#         print(number)

# Loop over ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# Use continue to skip "Saturday" and "Sunday" — print weekdays only.

# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# for day in days:
#     if day == "Saturday" or  day == "Sunday":
#         continue
#     else:
#         print(day)
# Loop over ["task1", "task2", "task3"] — if task is "task2" → do nothing (pass), else print "Working on taskX".

tasks = ["task1", "task2", "task3"]

for task in tasks:
    if task == "task2":
        pass
    else:
        print(f"working on {task}")
