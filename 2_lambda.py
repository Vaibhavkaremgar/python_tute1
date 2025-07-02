# python
# Copy
# Edit
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 2️⃣ Use filter() and a lambda function to keep only numbers greater than 5.

# 3️⃣ Print the result as a list.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Greater_numb = list(filter(lambda x: x > 5,numbers))
# print(Greater_numb)
# ou have a list of names:

# python
# Copy
# Edit
# names = ['Alice', 'bob', 'CHARLIE', 'daVid']
# Task:
# 1️⃣ Use map() and a lambda to make all names lowercase.
# 2️⃣ Sort the lowercase names alphabetically.
# 3️⃣ Print the final list.

# 👉 What you should write
# Try to write it in one or two lines if you can!
# Hint: map(lambda name: name.lower(), names) → returns a map object, so wrap it in list() if needed.

# Example structure:

# python
# Copy
# Edit
# names = ['Alice', 'bob', 'CHARLIE', 'daVid']

# # Step 1: map() to lowercase
# lower_names = _______

# # Step 2: sort the lowercase names
# sorted_names = _______

# print(sorted_names)sorted(pairs, key=lambda pair: pair[1])

# names = ['Alice', 'bob', 'CHARLIE', 'daVid']
# lower_names = list(map(lambda name: name.lower(),names))
# sorted_names = sorted(lower_names, key=lambda name: name[0])
# print(sorted_names)

# words = ['banana', 'apple', 'kiwi', 'pineapple', 'grape']

# sorted_words = sorted(words, key= lambda word: len(word))

# print(sorted_words)

# Max_word = max(words, key=lambda word:len(word))
# print(Max_word)
# Task:
# 1️⃣ Use filter() and a lambda to get only the words longer than 5 letters.
# 2️⃣ Convert the result to a list.
# 3️⃣ Print the list.
# words = ['banana', 'apple', 'kiwi', 'pineapple', 'grape', 'fig']
# larger_letter = list(filter(lambda word:len(word)>5,words))
# print(larger_letter)
# Do this in one small script:

# 1️⃣ Filter the list to keep only words longer than 5 letters.
# 2️⃣ Sort the filtered words by length, longest first.
# 3️⃣ Print the final list.

words = ['banana', 'apple', 'kiwi', 'pineapple', 'grape', 'fig', 'bluessberry', 'melon']
filtered_list = list(filter(lambda word: len(word)>5,words))
sorted_list = sorted(filtered_list,key=lambda word: len(word),reverse=True)
print(sorted_list)
