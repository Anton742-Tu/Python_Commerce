from src.base_product import BaseProduct
from src.logging_mixin import LoggingMixin


class Product(LoggingMixin, BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int, **kwargs):
        """
        Базовый класс продукта с логированием
        :param name: Название
        :param description: Описание
        :param price: Цена
        :param quantity: Количество
        """
        super().__init__(name=name, description=description, price=price, quantity=quantity, **kwargs)

    def __str__(self) -> str:
        """Строковое представление продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @property
    def additional_info(self) -> str:
        """Дополнительная информация (базовый вариант)"""
        return "Базовый продукт"

    @classmethod
    def create_product(cls, data: dict) -> "Product":
        """Создание продукта из словаря"""
        return cls(
            name=str(data["name"]),
            description=str(data["description"]),
            price=float(data["price"]),
            quantity=int(data["quantity"]),
        )
