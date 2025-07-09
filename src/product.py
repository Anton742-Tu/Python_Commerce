from decimal import Decimal
from typing import Any, Dict

from src.base_product import BaseProduct


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
        super().__init__(name, description, price, quantity)
        self.name = name
        self.description = description
        self.price = price
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
