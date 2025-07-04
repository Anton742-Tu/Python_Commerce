from typing import List, Optional, Type, Dict, Any, ClassVar
from src.product import Product
from src.base_container import BaseContainer


class Category(BaseContainer[Product]):
    """Класс категории продуктов"""

    product_count = None
    category_count = None
    _category_count: ClassVar[int] = 0
    _product_count: ClassVar[int] = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None):
        """
        Инициализация категории
        :param name: Название категории
        :param description: Описание категории
        :param products: Список продуктов (опционально)
        """
        super().__init__(name, description)
        self.product_count = None
        self.category_count = None
        self._items = products.copy() if products else []
        Category._category_count += 1
        Category._product_count += len(self._items)

    @property
    def items(self) -> List[Product]:
        """Реализация абстрактного свойства items"""
        return self._items

    @property
    def products(self) -> List[Product]:
        """Алиас для items для обратной совместимости"""
        return self._items

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Category":
        """Создает категорию из словаря"""
        from src.product import Product  # Локальный импорт

        products = [
            Product(
                name=str(p["name"]),
                description=str(p["description"]),
                price=float(p["price"]),
                quantity=int(p["quantity"]),
            )
            for p in data.get("products", [])
            if all(key in p for key in ["name", "description", "price", "quantity"])
        ]
        return cls(name=str(data["name"]), description=str(data["description"]), products=products)

    def add_product(self, product: Product, allowed_types: Optional[List[Type[Product]]] = None) -> None:
        """
        Добавляет продукт в категорию с проверкой типа

        Args:
            product: Объект продукта для добавления
            allowed_types: Список разрешенных типов продуктов

        Raises:
            TypeError: Если тип продукта не соответствует требованиям
            ValueError: Если продукт None
        """
        if product is None:
            raise ValueError("Нельзя добавить None в качестве продукта")

        if not isinstance(product, Product):
            raise TypeError(f"Ожидается Product, получен {type(product).__name__}")

        if allowed_types and not any(isinstance(product, t) for t in allowed_types):
            allowed_names = [t.__name__ for t in allowed_types]
            raise TypeError(f"Разрешены только: {', '.join(allowed_names)}. " f"Получен: {type(product).__name__}")

        self._items.append(product)

    @classmethod
    def reset_counters(cls) -> None:
        pass

    @classmethod
    def get_category_count(cls) -> None:
        pass

    @classmethod
    def get_product_count(cls) -> None:
        pass
