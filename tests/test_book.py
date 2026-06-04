# tests/test_book.py
import unittest
from unittest.mock import Mock
import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from book import BookCatalog
from book import Book, Genre

class TestBookCatalog(unittest.TestCase):

    def setUp(self):
        # Створюємо реальний об'єкт каталогу
        self.catalog = BookCatalog()
        
        # Мокаємо залежність (Book)
        self.mock_book1 = Mock()
        self.mock_book1.title = "1984"
        
        self.mock_book2 = Mock()
        self.mock_book2.title = "The Great Gatsby"

    def test_add_book(self):
        """Перевірка додавання книги до каталогу"""
        self.catalog.add_book(self.mock_book1)
        
        self.assertEqual(len(self.catalog.books), 1)
        self.assertIn(self.mock_book1, self.catalog.books)

    def test_get_books(self):
        """Перевірка отримання списку всіх книг (метод get_books)"""
        # Спочатку перевіряємо, що порожній каталог повертає порожній список
        self.assertEqual(len(self.catalog.get_books()), 0)
        self.assertEqual(self.catalog.get_books(), [])

        # Додаємо дві книги (моки)
        self.catalog.add_book(self.mock_book1)
        self.catalog.add_book(self.mock_book2)
        
        # Перевіряємо, чи get_books повертає саме ці дві книги
        books_list = self.catalog.get_books()
        self.assertEqual(len(books_list), 2)
        self.assertIn(self.mock_book1, books_list)
        self.assertIn(self.mock_book2, books_list)

    def test_search_by_title_found(self):
        """Перевірка пошуку існуючої книги"""
        self.catalog.add_book(self.mock_book1)
        self.catalog.add_book(self.mock_book2)
        
        result = self.catalog.search_by_title("gatsby")
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], self.mock_book2)

    def test_search_by_title_not_found(self):
        """Перевірка пошуку неіснуючої книги"""
        self.catalog.add_book(self.mock_book1)
        
        result = self.catalog.search_by_title("Harry Potter")
        
        self.assertEqual(len(result), 0)

class TestBook(unittest.TestCase):
    def test_book_initialization(self):
        """Перевірка ініціалізації об'єкта Book (щоб покрити рядки 13-17)"""
        # Створюємо реальну книгу
        book = Book(id=10, title="Кобзар", author="Тарас Шевченко", genre=Genre.FICTION)
        
        # Перевіряємо, чи всі поля правильно записалися
        self.assertEqual(book.id, 10)
        self.assertEqual(book.title, "Кобзар")
        self.assertEqual(book.author, "Тарас Шевченко")
        self.assertEqual(book.genre, Genre.FICTION)
        
        # За замовчуванням книга має бути доступною
        self.assertTrue(book.isAvailable)

if __name__ == '__main__':
    unittest.main()