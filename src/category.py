from __future__ import annotations
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from .product import Product


class Category:
    _category_count: int = 0
    _product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None):
        """
        Инициализация категории
        :param name: Название категории
        :param description: Описание категории
        :param products: Список товаров (опционально)
        """
        self.name = name
        self.description = description
        self.__products = products.copy() if products else []

        Category._category_count += 1
        Category._product_count += len(self.__products)

    def __str__(self) -> str:
        """
        Возвращает строковое представление категории с общим количеством товаров
        Формат: "Название категории, количество продуктов: X, общее количество товаров: Y"
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return (f"{self.name}, количество продуктов: {len(self.__products)}, "
                f"общее количество товаров: {total_quantity}")

    @property
    def products(self) -> str:
        """Возвращает строку с перечислением всех товаров"""
        return "\n".join(str(product) for product in self.__products)

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")
        self.__products.append(product)
        Category._product_count += 1

    @property
    def total_quantity(self) -> int:
        """Возвращает общее количество товаров в категории"""
        return sum(product.quantity for product in self.__products)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Category:
        """
        Создает категорию из словаря данных
        :param data: Словарь с данными категории
        :return: Объект Category
        :raises KeyError: Если отсутствуют обязательные поля
        """
        return cls(
            name=data["name"],
            description=data["description"],
            products=[Product.from_dict(p) for p in data.get("products", [])],
        )

    @classmethod
    def load_from_json(cls, file_path: str | Path) -> List[Category]:
        """
        Загружает категории из JSON файла
        :param file_path: Путь к JSON файлу
        :return: Список объектов Category
        :raises FileNotFoundError: Если файл не существует
        :raises json.JSONDecodeError: Если невалидный JSON
        :raises ValueError: Если некорректная структура данных
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise ValueError("JSON должен содержать список категорий")

            return [cls.from_dict(item) for item in data]

        except FileNotFoundError as e:
            raise FileNotFoundError(f"Файл {file_path} не найден") from e
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Ошибка декодирования JSON в файле {file_path}", e.doc, e.pos) from e

    @property
    def products_count(self) -> int:
        """Возвращает количество товаров в категории"""
        return len(self.__products)

    @classmethod
    def get_total_categories(cls) -> int:
        """Возвращает общее количество категорий"""
        return cls._category_count

    @classmethod
    def get_total_products(cls) -> int:
        """Возвращает общее количество товаров"""
        return cls.product_count

    def get_products_raw(self) -> List[Product]:
        """Возвращает список объектов Product (для сериализации)"""
        return self.__products.copy()

    @classmethod
    def reset_counters(cls) -> None:
        """Сбрасывает счетчики категорий и товаров"""
        cls._category_count = 0
        cls.product_count = 0

    def __len__(self) -> int:
        return self.products_count
