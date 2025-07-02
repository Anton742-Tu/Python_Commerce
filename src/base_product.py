from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Базовый абстрактный класс для всех продуктов"""
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
    def create_product(cls, data: dict) -> 'BaseProduct':
        """Абстрактный метод создания продукта из словаря"""
        pass

    def apply_discount(self, discount: float) -> None:
        """Общий метод для применения скидки"""
        if discount <= 0 or discount > 1:
            raise ValueError("Скидка должна быть между 0 и 1")
        self.price *= (1 - discount)
