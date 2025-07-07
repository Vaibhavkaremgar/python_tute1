# Create a new list of the squares of the even numbers.
# Use a list comprehension.

# Try it:

# python
# Copy
# Edit
# numbers = [1, 2, 3, 4, 5, 6]

# squares_of_evens = [x**2 for x in numbers if x % 2 == 0]

# print(squares_of_evens)

# words = ['apple', 'banana', 'cherry']
# first_letter = [x[0] for x in words ]
# print(first_letter)

# numbers = [1, 2, 3, 4, 5, 6]
# even_squares = [x**2 if x%2==0 else x for x in numbers]
# print(even_squares)

# Replace negative numbers with 0, keep positives unchanged.

# numbers = [1, -2, -3, 4, 5, -6]
# neg_num = [x*0 if x<0 else x for x in numbers]
# print(neg_num)

# matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# flat = [ inner_value for outer in matrix for inner_value in outer ]

# print(flat)

# a = 5
# five_table = [a*x for x in range(1,11) ]
# print(five_table)


# Given a list of words, count how many times each word appears — store the result in a dictionary.

# 📌 Example
# Input:

# python
# Copy
# Edit
# words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# Output:

# python
# Copy
# Edit
# {'apple': 3, 'banana': 2, 'orange': 1}
# 🔑 Key steps
# 1️⃣ Create an empty dictionary: counts = {}
# 2️⃣ Loop through each word in the list.
# 3️⃣ If the word is already a key → increase its count.
# 4️⃣ If not → add it with count 1.

# ✅ Try to fill this
# words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# counts = {}
# for word in words:
#     if word in counts:
#         counts[word]+=1
#     else:
#         counts[word]=1
# print(counts)

# numbers = [1, 7, 3, 8, 9, 6]

# diction = {}

# for i in numbers:
#     if i %2 == 0:
#         diction[i] = "even"
#     else:
#         diction[i] = "odd"
# print(diction)

numbers = [1, 7, 3, 8, 9, 6]

groups = {'even': [], 'odd': []}

for num in numbers:
    if num %2 == 0:
        groups['even'].append(num)
    else:
        groups['odd'].append(num)

print(groups)
