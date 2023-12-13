class Book:
    language = "English"  # Class-level variable

    def __init__(self, title, author):
        self.title = title  # Instance-level variable
        self.author = author  # Instance-level variable


book1 = Book("Python Crash Course", "Eric Matthes")
book2 = Book("Clean Code", "Robert C. Martin")

print(f"{book1.title} - {book1.author}, Language: {Book.language}")  # Output: Python Crash Course - Eric Matthes, Language: English
print(f"{book2.title} - {book2.author}, Language: {Book.language}")  # Output: Clean Code - Robert C. Martin, Language: English
