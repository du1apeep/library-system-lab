from catalog import Catalog
from notifications import EmailNotifier, NotificationManager
from user import Reader
from book import Book, Genre


def main():
    my_catalog = Catalog()

    noti = NotificationManager()

    book1 = Book(1, "The Great Gatsby", "F. Scott Fitzgerald", Genre.FICTION)
    reader1 = Reader(1, "Alice", "alice@example.com")

    my_catalog.catalog.add_book(book1)
    notifier = EmailNotifier(reader1.email)
    noti.attach(notifier)

    print("--- 1. ПЕРЕВІРКА КАТАЛОГУ ---")
    # Перевіряємо, чи дійсно книга додалася, шукаючи її за назвою
    # (припускаю, що у вашому BookCatalog є метод search_by_title)
    found_books = my_catalog.catalog.search_by_title("Gatsby")
    if found_books:
        print(
            f"Успіх! Книгу знайдено: '{found_books[0].title}', Автор: {found_books[0].author}")
    else:
        print("Книгу не знайдено у каталозі.")

    print("\n--- 2. ПЕРЕВІРКА СПОВІЩЕНЬ (OBSERVER) ---")
    # Викликаємо notify, щоб усі підписники (наш EmailNotifier) отримали повідомлення
    message = f"Шановна {reader1.name}, нове надходження: '{book1.title}'!"
    noti.notify(message)

    print("\n--- 3. ПЕРЕВІРКА СИНГЛТОНУ (SINGLETON) ---")
    # Створюємо нібито "новий" каталог
    catalog2 = Catalog()

    # Перевіряємо, чи це той самий об'єкт у пам'яті
    if my_catalog is catalog2:
        print("Успіх! Catalog працює як Singleton (це один і той самий об'єкт).")
    else:
        print("Помилка: Синглтон не працює, створено різні об'єкти.")


if __name__ == "__main__":
    main()
