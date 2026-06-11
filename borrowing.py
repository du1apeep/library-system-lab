from datetime import datetime, timedelta
from book import Book
from user import Reader


class BorrowingItem:
    def __init__(self, book: Book):
        self.book = book
        self.due_date = datetime.now() + timedelta(days=14)  # на 2 тижні
        self.return_date = None


class Borrowing:
    def __init__(self, reader: Reader):
        self.reader = reader
        self.items = []

    def borrow_book(self, book: Book):
        if book.isAvailable:
            book.isAvailable = False
            item = BorrowingItem(book)
            self.items.append(item)
            print(f"{self.reader.name} borrowed '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is currently unavailable.")

    def return_book(self, book: Book):
        for item in self.items:
            if item.book == book and item.return_date is None:
                item.return_date = datetime.now()
                book.isAvailable = True
                print(f"{self.reader.name} returned '{book.title}'")
                return
        print(
            f"{self.reader.name} did not borrow '{book.title}' or has already returned it.")
