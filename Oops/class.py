# Write a Car class with:

# Attributes: brand, model, year

# Method: description() which prints the car’s details

class Car():
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def car_features(self):
        print(f"The {self.brand} car manufactured in {self.year} is a {self.model}")
car1 = Car("baleno","sigma varient",2020)
car1.car_features()
car2 = Car("hundai","mid varient",2023)
car2.car_features()

# Practice Example 1: Book Class
# Create a Book class with:

# Attributes: title, author, pages

# Method: book_info() that prints the book details
class Book():
    def __init__(self,title,author,pages,price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
    def book_details(self):
        print(f"The {self.title} book written by {self.author} has {self.pages} pages that costs {self.price}")

Book1 = Book("na savu nen sastha","koushik",420,360)
Book1.book_details()