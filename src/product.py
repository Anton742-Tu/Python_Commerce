from abc import ABC, abstractmethod
from decimal import Decimal
from typing import Dict, Any


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int, **kwargs: Any) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод строкового представления"""
        pass

    @property
    @abstractmethod
    def additional_info(self) -> str:
        """Абстрактное свойство с дополнительной информацией"""
        pass

    @classmethod
    @abstractmethod
    def create_product(cls, data: Dict[str, Any]) -> "BaseProduct":
        """Абстрактный метод создания продукта из словаря"""
        pass

    def apply_discount(self, discount: float) -> None:
        """Общий метод для применения скидки"""
        if discount <= 0 or discount > 1:
            raise ValueError("Скидка должна быть между 0 и 1")
        self.price = float(Decimal(str(self.price)) * (1 - Decimal(str(discount))))


class Product(BaseProduct):
    """Конкретная реализация продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int, **kwargs: Any) -> None:
        """
        Инициализация продукта
        :param name: Название продукта
        :param description: Описание продукта
        :param price: Цена продукта (должна быть положительной)
        :param quantity: Количество продукта (неотрицательное)
        :param kwargs: Дополнительные параметры
        """
        super().__init__(name, description, price, quantity, **kwargs)
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Строковое представление продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @property
    def additional_info(self) -> str:
        """Дополнительная информация о продукте"""
        return "Базовый продукт"

    @classmethod
    def create_product(cls, data: Dict[str, Any]) -> "Product":
        """Создание продукта из словаря"""
        return cls(
            name=str(data["name"]),
            description=str(data["description"]),
            price=float(data["price"]),
            quantity=int(data["quantity"]),
        )
