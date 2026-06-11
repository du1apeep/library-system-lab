from book import Book


class User:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email


class Reader(User):
    def __init__(self, id: int, name: str, email: str):
        super().__init__(id, name, email)

    def search_book(self, catalog, title: str):
        return catalog.search_by_title(title)


class Librarian(User):
    def __init__(self, id: int, name: str, email: str):
        super().__init__(id, name, email)

    def add_book(self, catalog, book: Book):
        catalog.add_book(book)
