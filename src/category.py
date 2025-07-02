from __future__ import annotations
from typing import List, Optional
from src.product import Product


class Category:
    _category_count: int = 0
    _product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None):
        """
        Initialize a category with name, description, and optional list of products.

        Args:
            name: Category name
            description: Category description
            products: Optional list of Product objects
        """
        self.name = name
        self.description = description
        self.__products = products.copy() if products else []

        Category._category_count += 1
        Category._product_count += len(self.__products)

    @classmethod
    def from_dict(cls, data: dict) -> Category:
        """Create a category from a dictionary"""
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
        """Return total number of categories created"""
        return cls._category_count

    @classmethod
    def get_product_count(cls) -> int:
        """Return total number of products across all categories"""
        return cls._product_count

    def add_product(self, product: Product, allowed_types: list[type[Product]] = None) -> None:
        """
        Add a product to the category with type checking

        Args:
            product: Product to add
            allowed_types: List of allowed product types

        Raises:
            TypeError: If product type doesn't match restrictions
        """
        if not isinstance(product, Product):
            raise TypeError("Can only add objects of Product class or its subclasses")

        if allowed_types and not isinstance(product, tuple(allowed_types)):
            allowed_names = [t.__name__ for t in allowed_types]
            raise TypeError(
                f"Only products of these types are allowed: {', '.join(allowed_names)}. "
                f"Received: {type(product).__name__}"
            )

        self.__products.append(product)
        Category._product_count += 1

    @property
    def products(self) -> List[Product]:
        """Return the list of products in this category"""
        return self.__products

    def __str__(self) -> str:
        """String representation of the category"""
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    @classmethod
    def reset_counters(cls) -> None:
        """Reset category and product counters"""
        cls._category_count = 0
        cls._product_count = 0

    @property
    def category_count(self):
        return self._category_count

    @property
    def product_count(self):
        return self._product_count
