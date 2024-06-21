# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, chapterTitles, price = None):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.chapterTitles = chapterTitles
        self.__secret = "this is secret attribute"

    # TODO: create instance methods
    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    def getChapters(self):
        return self.chapterTitles
    def setDiscount(self, amount):
        self._discount = amount #attribute internal to class NOT TO BE USED OUTSIDE

# TODO: create some book instances
b1 = Book("War and Peace", "Tolstoy", 1225, chapterTitles = ["Chapter 1", "chapter 2", "chapter 3"], price = 59.95)
b2 = Book("The Catcher in the Rye", "JD Sallinger", 234, chapterTitles = ["Chapter 1", "chapter 2", "chapter 3"], price = 29.95)

# TODO: print the price of book1
print(b1.getPrice())
print(b1.getChapters())

# TODO: try setting the discount
b2.setDiscount(.25)
print(b2.getPrice())

# TODO: properties with double underscores are hidden by the interpreter
print(b2._Book__secret)

