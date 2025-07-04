from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic
from src.product import Product

T = TypeVar("T", bound=Product)


class BaseContainer(ABC, Generic[T]):
    """Абстрактный базовый класс для контейнеров продуктов"""

    @abstractmethod
    def __init__(self, name: str, description: str = "") -> None:
        self.name: str = name
        self.description: str = description
        self._items: List[T] = []

    @property
    @abstractmethod
    def items(self) -> List[T]:
        """Абстрактное свойство для доступа к элементам"""
        pass

    @property
    def total_value(self) -> float:
        """Общая стоимость всех элементов"""
        return sum(item.price * item.quantity for item in self._items)

    def __str__(self) -> str:
        """Строковое представление"""
        return f"{self.name}, количество элементов: {len(self._items)}, общая стоимость: {self.total_value:.2f} руб."
