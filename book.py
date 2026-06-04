from enum import Enum

class Genre(Enum):
    FICTION = "Fiction"
    NON_FICTION = "Non-Fiction"
    SCIENCE_FICTION = "Science Fiction"
    FANTASY = "Fantasy"
    MYSTERY = "Mystery"
    DETECTIVE = "Detective"

class Book:
    def __init__(self, id: int, title: str, author: str, genre: Genre, isAvailable: bool = True):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.isAvailable = isAvailable

class BookCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def get_books(self):
        return self.books
    
    def search_by_title(self, title: str):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def get_description(self): pass
