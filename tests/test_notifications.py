# tests/test_notifications.py
from notifications import NotificationManager, EmailNotifier
import unittest
from unittest.mock import Mock, patch
import sys
import os

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


class TestNotificationManager(unittest.TestCase):

    def setUp(self):
        """Підготовка для тестування Subject (Видавця)"""
        self.manager = NotificationManager()

        # Мокаємо залежності: нам не потрібні реальні EmailNotifier,
        # створюємо абстрактних "спостерігачів"
        self.mock_observer1 = Mock()
        self.mock_observer2 = Mock()

    def test_attach_observer(self):
        """Перевірка додавання підписника"""
        self.manager.attach(self.mock_observer1)

        self.assertEqual(len(self.manager._observers), 1)
        self.assertIn(self.mock_observer1, self.manager._observers)

    def test_attach_duplicate_observer(self):
        """Перевірка того, що дублікати підписників не додаються"""
        self.manager.attach(self.mock_observer1)
        # Намагаємося додати того ж самого підписника вдруге
        self.manager.attach(self.mock_observer1)

        # Список має містити лише 1 елемент
        self.assertEqual(len(self.manager._observers), 1)

    def test_detach_observer(self):
        """Перевірка видалення підписника"""
        self.manager.attach(self.mock_observer1)
        self.manager.attach(self.mock_observer2)

        # Видаляємо першого
        self.manager.detach(self.mock_observer1)

        self.assertEqual(len(self.manager._observers), 1)
        self.assertNotIn(self.mock_observer1, self.manager._observers)
        self.assertIn(self.mock_observer2, self.manager._observers)

    def test_notify_observers(self):
        """Перевірка розсилки повідомлень всім підписникам"""
        self.manager.attach(self.mock_observer1)
        self.manager.attach(self.mock_observer2)

        test_message = "Нова книга доступна!"
        self.manager.notify(test_message)

        # Перевіряємо, чи викликався метод update()
        # у КОЖНОГО підписника з правильним текстом
        self.mock_observer1.update.assert_called_once_with(test_message)
        self.mock_observer2.update.assert_called_once_with(test_message)


class TestEmailNotifier(unittest.TestCase):

    def setUp(self):
        """Підготовка для тестування конкретного Спостерігача"""
        self.email_notifier = EmailNotifier("test@example.com")

    # Використовуємо patch, щоб перехопити виклик функції print()
    @patch('builtins.print')
    def test_update_prints_correct_message(self, mock_print):
        """Перевірка роботи методу update() (чи правильно формується повідомлення)"""

        test_message = "Ваш термін оренди закінчується."
        self.email_notifier.update(test_message)

        # Перевіряємо, чи викликав метод print()
        # правильний текст
        expected_output = ("Email sent to test@example.com: "
                           "Ваш термін оренди закінчується.")
        mock_print.assert_called_once_with(expected_output)


if __name__ == '__main__':
    unittest.main()
