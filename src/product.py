from __future__ import annotations


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __add__(self, other: Product) -> float:
        """
        Сложение двух продуктов одного класса
        :param other: Второй объект для сложения
        :return: Сумма произведений цены на количество
        :raises TypeError: Если объекты разных классов
        """
        if not isinstance(other, self.__class__):
            raise TypeError(f"Нельзя складывать {self.__class__.__name__} и {other.__class__.__name__}")

        return (self.price * self.quantity) + (other.price * other.quantity)

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __eq__(self, other: object) -> bool:
        """Проверка на равенство продуктов (по названию)"""
        if not isinstance(other, Product):
            return False
        return self.name == other.name

    @classmethod
    def from_dict(cls, p):
        pass
