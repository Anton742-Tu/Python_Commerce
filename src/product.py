from __future__ import annotations
from typing import Dict, Any


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
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Сеттер для цены с подтверждением понижения
        :param new_price: Новая цена товара
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            print(f"Внимание! Понижение цены с {self.__price} до {new_price}")
            confirmation = input("Подтвердите понижение цены (y/n): ").strip().lower()
            if confirmation != "y":
                print("Изменение цены отменено")
                return

        self.__price = new_price
        print(f"Цена успешно изменена на {new_price}")

    @classmethod
    def new_product(cls, product_data: Dict[str, Any]) -> Product:
        """
        Создает продукт из словаря данных
        :param product_data: Словарь с параметрами продукта
        :return: Объект Product
        :raises ValueError: Если отсутствуют обязательные поля
        """
        required_fields = {"name", "description", "price", "quantity"}
        if missing := required_fields - set(product_data.keys()):
            raise ValueError(f"Отсутствуют обязательные поля: {missing}")

        return cls(
            name=str(product_data["name"]),
            description=str(product_data["description"]),
            price=float(product_data["price"]),
            quantity=int(product_data["quantity"]),
        )

    def __str__(self) -> str:
        """Строковое представление продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def from_dict(cls, p):  # type: ignore
        pass
