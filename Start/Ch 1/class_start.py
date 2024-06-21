# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    # TODO: double-underscore properties are hidden from other classes
    __booklist = None
    # TODO: create a class method
    @classmethod 
    def getBookTypes(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method
    def getBookList():
        if Book.__booklist == None:
            Book.__bookList = []
        return Book.__bookList
    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid booktype")
        else:
            self.booktype = booktype


# TODO: access the class attribute
print("booktypes: ", Book.getBookTypes())

# TODO: Create some book instances
b1 = Book("Title of Book", "EBOOK")
b2 = Book("The Eye of the World", "PAPERBACK")
b3 = Book("A Memory of Light", "EBOOK")

# TODO: Use the static method to access a singleton object
thebooks = Book.getBookList()

bookshelf = [b1, b2, b3]
for b in bookshelf:
    if b.booktype == "EBOOK":
        thebooks.append(b)

for b in thebooks:
    print(b.title)