# import argparse

# parser = argparse.ArgumentParser(description="Greeting Script")

# parser.add_argument("name", help="Your name")
# parser.add_argument("age", type=int, help="Your age")
# parser.add_argument("--country", default="India", help="Your country")
# parser.add_argument("--debug", action="store_true", help="Enable debug mode")

# args = parser.parse_args()

# print(f"Hello, {args.name}, aged {args.age}, from {args.country}!")

# if args.debug:
#     print("Debug mode is ON")
# Write a Python script using argparse that:

# Accepts two numbers as required positional arguments.

# Accepts an optional flag --multiply that:

# If used, prints the product of the two numbers.

# If not used, prints the sum of the two numbers.

# parser = argparse.ArgumentParser(description="mul or addition of 2 num")

# parser.add_argument("num1", type=int, help="first number")
# parser.add_argument("num2", type=int, help="second number")
# parser.add_argument("--multiply",action="store_true",help="multiply instead of addition")
# args = parser.parse_args()

# if args.multiply:
#     print("product is", args.num1 * args.num2)
# else:
#     print("sum is : -", args.num1 + args.num2)

import requests

response = requests.get("https://api.github.com")

data = response.json()

# print("Current user url:", data["current_user_url"])
# print("Repository search url:", data["repository_search_url"])
print("total repos found:", data["total_count"])
print("top repos:", data["items"][0]["full name"])
print("top repo stars:", data["items"][0]["stargazers_count"])