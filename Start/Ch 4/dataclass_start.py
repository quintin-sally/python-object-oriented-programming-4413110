# Python Object Oriented Programming by Joe Marini course example
# Using data classes to represent data objects
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float
    
    def bookinfo(self):
        return f"{self.title} by {self.author} is {self.pages} long and costs ${self.price}"

# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# access fields
print(b1.title)
print(b2.author)

# TODO: print the book itself - dataclasses AUTOMATICALLY implements __repr__
print(b1)
print(b2)

# TODO: comparing two dataclasses - they AUTOMATICALLY implements __eq__
b3 = b1
print(b1 == b3)

# TODO: change some fields

b3.title = "A memory of light"
b3.pages = 12634

print(b3.bookinfo())