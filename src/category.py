from typing import List, Dict, Any, Optional
from product import Product


class Category:
    _category_count = 0
    _product_count = 0

    def init(self, name: str, description: str, products: Optional[List[Product]] = None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        Category._category_count += 1
        Category._product_count += len(self.__products)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Category:
        """Создает категорию из словаря данных"""
        from src.product import Product  # Локальный импорт для избежания циклических зависимостей
        products = [Product.from_dict(product_data) for product_data in data.get('products', [])]
        return cls(
            name=data['name'],
            description=data['description'],
            products=products
        )


    @classmethod
    def load_from_json(cls, file_path: str) -> List[Category]:
        """Загружает категории из JSON файла"""
        import json
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return [cls.from_dict(category_data) for category_data in data]


    @classmethod
    def reset_counters(cls) -> None:
        cls._category_count = 0
        cls._product_count = 0

    @property
    def products(self) -> List[Product]:
        return self.__products

    @property
    def category_count(self) -> int:
        return Category._category_count

    @property
    def product_count(self) -> int:
        return Category._product_count

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category._product_count += 1

    def __len(self) -> int:
        return len(self.products)

    def __str(self) -> str:
        return f"{self.name}, количество продуктов: {len(self)} шт."
