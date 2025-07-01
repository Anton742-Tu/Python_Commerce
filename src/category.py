from __future__ import annotations

from typing import List, Optional

from src.product import Product


class Category:
    product_count = None
    _category_count: int = 0
    _product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None):
        self._Category__products = None
        self.name = name
        self.description = description
        self.__products = products.copy() if products else []

        Category._category_count += 1
        Category._product_count += len(self.__products)

    @classmethod
    def from_dict(cls, data: dict) -> Category:
        """Создает категорию из словаря (без загрузки файла)"""
        from .product import Product  # Локальный импорт во избежание циклических зависимостей

        products = [
            Product(
                name=str(p["name"]),
                description=str(p["description"]),
                price=float(p["price"]),
                quantity=int(p["quantity"]),
            )
            for p in data.get("products", [])
        ]
        return cls(name=str(data["name"]), description=str(data["description"]), products=products)

    @classmethod
    def get_category_count(cls) -> int:
        """Возвращает общее количество категорий"""
        return cls._category_count

    @classmethod
    def get_product_count(cls) -> int:
        """Возвращает общее количество товаров"""
        return cls._product_count

    def add_product(self, product: Product, allowed_types: list[type[Product]] = None) -> None:
        """
        Добавляет продукт в категорию с проверкой типа через type()
        :param product: Добавляемый продукт
        :param allowed_types: Список разрешённых типов (классов)
        :raises TypeError: Если тип продукта не соответствует ограничениям
        """
        # Проверка базового типа через type()
        if type(product) not in (Product, *Product.__subclasses__()):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

        # Проверка ограничений по типам
        if allowed_types:
            product_type = type(product)
            if not any(product_type is t for t in allowed_types):
                allowed_names = [t.__name__ for t in allowed_types]
                raise TypeError(
                    f"Разрешены только продукты конкретных типов: {', '.join(allowed_names)}. "
                    f"Получен: {product_type.__name__}"
                )

        self.__products.append(product)
        Category._product_count += 1

    @property
    def products(self) -> str:
        """Возвращает строковое представление товаров"""
        return "\n".join(str(p) for p in self.__products)

    def __str__(self) -> str:
        """Строковое представление категории"""
        return f"{self.name}, количество продуктов: {len(self.__products)}"

    @classmethod
    def reset_counters(cls) -> None:
        """Сбрасывает счётчики категорий и товаров"""
        cls._category_count = 0
        cls._product_count = 0

    @property
    def Category__products(self):
        return self._Category__products
