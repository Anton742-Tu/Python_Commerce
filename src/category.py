import logging
from typing import List, Optional, Type

from mypy.reachability import TypeVar

from src.exceptions import ZeroQuantityError
from src.product import Product

T = TypeVar("T", bound=Product)


class Category:
    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None):
        self.name = name
        self.description = description
        self._products = products if products is not None else []
        self.logger = logging.getLogger("Category")
        self.logger.setLevel(logging.INFO)

        # Добавляем обработчик, если его нет
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter("%(name)s - %(message)s"))
            self.logger.addHandler(handler)

    @classmethod
    def from_dict(cls, data: dict) -> "Category":
        """Создает категорию из словаря"""
        from src.product import Product  # Локальный импорт во избежание циклических зависимостей

        # Проверяем обязательные поля
        if "name" not in data or "description" not in data:
            raise ValueError("Отсутствуют обязательные поля 'name' или 'description'")

        # Обрабатываем продукты
        products = []
        if "products" in data:
            for product_data in data["products"]:
                try:
                    products.append(
                        Product(
                            name=str(product_data["name"]),
                            description=str(product_data["description"]),
                            price=float(product_data["price"]),
                            quantity=int(product_data["quantity"]),
                        )
                    )
                except (KeyError, ValueError) as e:
                    raise ValueError(f"Ошибка создания продукта: {str(e)}")

        return cls(name=str(data["name"]), description=str(data["description"]), products=products)

    @property
    def products(self) -> List[Product]:
        return self._products

    def add_product(self, product: Product, allowed_types: Optional[List[Type[Product]]] = None) -> None:
        """Добавляет товар в категорию с проверкой типа"""
        if product is None:
            raise ValueError("Нельзя добавить None в качестве товара")

        self.logger.info(f"Начало добавления товара: {product.name}")

        try:
            if not isinstance(product, Product):
                raise TypeError("Можно добавлять только объекты класса Product")

            if product.quantity <= 0:
                raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен")

            if allowed_types and not any(isinstance(product, t) for t in allowed_types):
                allowed_names = [t.__name__ for t in allowed_types]
                raise TypeError(f"Разрешены только: {', '.join(allowed_names)}")

            self._products.append(product)
            self.logger.info(f"Товар '{product.name}' успешно добавлен")

        except (ZeroQuantityError, TypeError) as e:
            self.logger.error(str(e))
            raise
        finally:
            self.logger.info("Обработка добавления товара завершена")

    def get_average_price(self) -> float:
        """Рассчитывает среднюю цену товаров"""
        if not self._products:
            self.logger.info("Категория пуста, средняя цена: 0")
            return 0.0

        valid_products = [p for p in self._products if p.quantity > 0]
        if not valid_products:
            self.logger.info("Нет товаров с положительным количеством, средняя цена: 0")
            return 0.0

        total_price = sum(p.price * p.quantity for p in valid_products)
        total_quantity = sum(p.quantity for p in valid_products)
        average = total_price / total_quantity
        self.logger.info(f"Средняя цена: {average:.2f}")
        return average
