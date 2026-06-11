# tests/test_catalog.py
from catalog import Catalog
import unittest
from unittest.mock import patch
import sys
import os

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


class TestCatalogSingleton(unittest.TestCase):

    def setUp(self):
        """
        Підготовка до тесту.
        ОБОВ'ЯЗКОВО обнуляємо екземпляр Синглтона перед кожним тестом,
        щоб тести були незалежними один від одного.
        """
        Catalog._instance = None

    # Використовуємо patch, щоб підмінити реальний
    # BookCatalog на Mock під час ініціалізації
    @patch('catalog.BookCatalog')
    def test_singleton_instance_creation(self, mock_book_catalog):
        """1. Перевірка, що створюється лише один об'єкт (Singleton)"""

        # Створюємо нібито "два" різні каталоги
        catalog1 = Catalog()
        catalog2 = Catalog()

        # assertIs перевіряє, чи вказують обидві змінні
        # на ОДНУ І ТУ САМУ ділянку пам'яті
        self.assertIs(catalog1, catalog2)

        # Перевіряємо, чи внутрішній BookCatalog створювався лише ОДИН раз
        # (доводить, що блок ініціалізації в __new__ спрацював лише для першого виклику)
        mock_book_catalog.assert_called_once()

    def test_singleton_state_sharing(self):
        """2. Перевірка того, що стан (дані) є спільним для всіх звернень"""
        catalog1 = Catalog()
        catalog2 = Catalog()

        # Змінюємо стан через перший об'єкт (наприклад, додаємо фейкового читача)
        catalog1.readers.append("Fake Reader")

        # Перевіряємо, чи другий об'єкт "бачить" цю зміну
        self.assertEqual(len(catalog2.readers), 1)
        self.assertIn("Fake Reader", catalog2.readers)

    def test_singleton_initial_attributes(self):
        """3. Перевірка правильної ініціалізації внутрішніх структур даних"""
        catalog = Catalog()

        # Перевіряємо, що списки читачів та видач створюються як порожні масиви
        self.assertIsInstance(catalog.readers, list)
        self.assertEqual(len(catalog.readers), 0)

        self.assertIsInstance(catalog.borrowings, list)
        self.assertEqual(len(catalog.borrowings), 0)


if __name__ == '__main__':
    unittest.main()
