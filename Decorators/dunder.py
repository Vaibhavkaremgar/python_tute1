# Try building a Book class with these dunder methods:

# __init__: to store title and author

# __str__: to print title by author

# __eq__: to compare if two books are the same based on title

# __len__: to return a fake page count (just for practice)

class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return (f"the book {self.title} was written by {self.author}")
    def __eq__(self, value):
        return self.title.lower()== value.lower()
    def __len__(self):
        return self.pages
B1=Book("ramayana","valmiki",300)
print(str(B1))
print(B1.__eq__("ramayana"))
print(B1.__eq__("Mahabharata"))
print(B1.__eq__("Ramayana"))
print(len(B1))
