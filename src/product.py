from abc import ABC, abstractmethod
from decimal import Decimal
from typing import Any, Dict


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализация продукта

        Args:
            name: Название продукта
            description: Описание продукта
            price: Цена продукта (должна быть положительной)
            quantity: Количество продукта не может быть отрицательным
            kwargs: Дополнительные параметры

        Raises:
            ValueError: Если количество ≤ 0 или цена ≤ 0
        """
        self.price = price
        if quantity <= 0:  # Разрешаем 0, но не отрицательные значения
            raise ValueError("Количество не может быть отрицательным")
        if price <= 0:
            raise ValueError("Цена должна быть положительной")

        self.name = name
        self.description = description
        self._price = Decimal(str(price))
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


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int, **kwargs: Any) -> None:
        """
        Инициализация продукта

        Args:
            name: Название продукта
            description: Описание продукта
            price: Цена продукта (положительная)
            quantity: Количество продукта (положительное)
            kwargs: Дополнительные атрибуты
        """
        if price <= 0:
            raise ValueError("Цена должна быть положительной")
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным")

        self.name = name
        self.description = description
        self._price = Decimal(str(price))
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Возвращает цену продукта"""
        return float(self._price)

    @price.setter
    def price(self, value: float) -> None:
        """Устанавливает цену продукта"""
        if value <= 0:
            raise ValueError("Цена должна быть положительной")
        self._price = Decimal(str(value))

    def __str__(self) -> str:
        """Строковое представление продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @property
    def additional_info(self) -> str:
        """Дополнительная информация о продукте"""
        return "Базовый продукт"

    @classmethod
    def create_product(cls, data: Dict[str, Any]) -> "Product":
        """Создает продукт из словаря"""
        return cls(
            name=str(data["name"]),
            description=str(data["description"]),
            price=float(data["price"]),
            quantity=int(data["quantity"]),
        )

    def apply_discount(self, discount: float) -> None:
        """
        Применяет скидку к цене продукта

        Args:
            discount: Размер скидки (от 0 до 1)
        """
        if not 0 < discount <= 1:
            raise ValueError("Скидка должна быть между 0 и 1")
        self._price = self._price * (Decimal("1") - Decimal(str(discount)))
