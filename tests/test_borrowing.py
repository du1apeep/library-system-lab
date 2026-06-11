import unittest
from unittest.mock import Mock
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from borrowing import Borrowing

class TestBorrowing(unittest.TestCase):

    def setUp(self):
        # 1. МОКАЄМО ЗАЛЕЖНОСТІ (Reader та Book) замість створення реальних об'єктів
        self.mock_reader = Mock()
        self.mock_reader.name = "Alice"  # Задаємо ім'я, бо воно використовується у print()

        self.mock_book = Mock()
        self.mock_book.title = "The Great Gatsby"
        self.mock_book.isAvailable = False  # Імітуємо, що книга спочатку доступна

        # 2. Створюємо реальний об'єкт, який ТЕСТУЄМО
        self.borrowing = Borrowing(self.mock_reader)

    def test_borrow_book_success(self):
        """Перевірка успішного взяття книги (mock_book.isAvailable == True)"""
        self.borrowing.borrow_book(self.mock_book)
        
        # Перевіряємо, чи змінився стан нашого мок-об'єкта книги
        self.assertFalse(self.mock_book.isAvailable)
        # Перевіряємо, чи додався запис у список items
        self.assertEqual(len(self.borrowing.items), 1)
        self.assertEqual(self.borrowing.items[0].book, self.mock_book)

    def test_borrow_book_unavailable(self):
        """Перевірка спроби взяти недоступну книгу"""
        # Імітуємо ситуацію, коли книга вже видана кимось іншим
        self.mock_book.isAvailable = False 
        
        self.borrowing.borrow_book(self.mock_book)
        
        # Список видач має залишитися порожнім
        self.assertEqual(len(self.borrowing.items), 0)

    def test_return_book_success(self):
        """Перевірка успішного повернення книги"""
        # Спочатку беремо книгу (налаштовуємо початковий стан)
        self.borrowing.borrow_book(self.mock_book)
        
        # Повертаємо книгу
        self.borrowing.return_book(self.mock_book)
        
        # Перевіряємо результати
        self.assertTrue(self.mock_book.isAvailable)
        self.assertIsNotNone(self.borrowing.items[0].return_date)

if __name__ == '__main__':
    unittest.main()