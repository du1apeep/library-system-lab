from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, book_title: str):
        pass


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self, book_title: str):
        pass


class NotificationManager(Subject):
    def __init__(self):
        self._observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        for observer in self._observers:
            observer.update(message)


class EmailNotifier(Observer):
    def __init__(self, email: str):
        self.email = email

    def update(self, message: str) -> None:
        print(f"Email sent to {self.email}: {message}")
