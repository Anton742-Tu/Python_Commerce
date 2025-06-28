from __future__ import annotations
from typing import Union


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализация продукта
        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара
        :param quantity: Количество товара
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __add__(self, other: Product) -> float:
        """
        Сложение двух продуктов (возвращает суммарную стоимость)
        :param other: Второй объект Product для сложения
        :return: Сумма произведений цены на количество
        :raises TypeError: Если other не является Product
        """
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")

        return (self.price * self.quantity) + (other.price * other.quantity)

    def __str__(self) -> str:
        """Строковое представление продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __eq__(self, other: object) -> bool:
        """Проверка на равенство продуктов (по названию)"""
        if not isinstance(other, Product):
            return False
        return self.name == other.name
