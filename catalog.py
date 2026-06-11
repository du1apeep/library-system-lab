from book import BookCatalog


class Catalog:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Catalog, cls).__new__(cls)
            # Ініціалізація
            cls._instance.catalog = BookCatalog()
            cls._instance.readers = []
            cls._instance.borrowings = []
        return cls._instance
