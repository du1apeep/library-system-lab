# tests/test_user.py
from user import Reader, Librarian
import unittest
from unittest.mock import Mock
import sys
import os

# Додаємо шлях до кореневої папки
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


class TestUser(unittest.TestCase):

    def setUp(self):
        """Підготовка ізольованих даних для тестів"""
        # Створюємо реальних користувачів
        self.reader = Reader(id=1, name="Alice", email="alice@example.com")
        self.librarian = Librarian(id=2, name="Bob", email="bob@example.com")

        # Мокаємо залежність: Каталог
        self.mock_catalog = Mock()

        # Мокаємо залежність: Книга
        self.mock_book = Mock()
        self.mock_book.title = "1984"

    # --- ТЕСТИ ДЛЯ ЧИТАЧА (Reader) ---

    def test_reader_initialization(self):
        """1. Перевірка правильної ініціалізації Читача (наслідування від User)"""
        self.assertEqual(self.reader.id, 1)
        self.assertEqual(self.reader.name, "Alice")
        self.assertEqual(self.reader.email, "alice@example.com")

    def test_reader_search_book_success(self):
        """2. Перевірка успішного пошуку книги читачем"""
        # Налаштовуємо мок каталогу: коли викликають search_by_title,
        # повертаємо список з нашою книгою
        self.mock_catalog.search_by_title.return_value = [self.mock_book]

        # Викликаємо метод читача
        result = self.reader.search_book(self.mock_catalog, "1984")

        # Перевіряємо, чи повернулася книга
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], self.mock_book)

        # Перевіряємо, чи читач дійсно викликав метод каталогу з правильним аргументом
        self.mock_catalog.search_by_title.assert_called_once_with("1984")

    def test_reader_search_book_not_found(self):
        """3. Перевірка пошуку книги, якої немає"""
        # Налаштовуємо мок каталогу: повертаємо порожній список
        self.mock_catalog.search_by_title.return_value = []

        result = self.reader.search_book(self.mock_catalog, "Unknown Book")

        # Перевіряємо результати
        self.assertEqual(len(result), 0)
        self.mock_catalog.search_by_title.assert_called_once_with(
            "Unknown Book")

    # --- ТЕСТИ ДЛЯ БІБЛІОТЕКАРЯ (Librarian) ---

    def test_librarian_initialization(self):
        """4. Перевірка правильної ініціалізації Бібліотекаря"""
        self.assertEqual(self.librarian.id, 2)
        self.assertEqual(self.librarian.name, "Bob")
        self.assertEqual(self.librarian.email, "bob@example.com")

    def test_librarian_add_book_success(self):
        """5. Перевірка успішного додавання книги бібліотекарем"""
        # Викликаємо метод бібліотекаря
        self.librarian.add_book(self.mock_catalog, self.mock_book)

        # Перевіряємо, чи бібліотекар дійсно передав цю книгу в каталог
        self.mock_catalog.add_book.assert_called_once_with(self.mock_book)

    def test_librarian_add_book_error_handling(self):
        """6. Перевірка реакції бібліотекаря на помилку від каталогу (дублікат)"""
        # Налаштовуємо мок каталогу: при виклику add_book викликати помилку
        self.mock_catalog.add_book.side_effect = ValueError(
            "Ця книга вже є в каталозі!")

        # Перевіряємо, чи помилка "прокидається" нагору, коли бібліотекар додає дублікат
        with self.assertRaises(ValueError):
            self.librarian.add_book(self.mock_catalog, self.mock_book)

        self.mock_catalog.add_book.assert_called_once_with(self.mock_book)


if __name__ == '__main__':
    unittest.main()
