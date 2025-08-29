import unittest
from src.product import Product
from src.base_product import BaseProduct


class MockProduct(BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name, description, price, quantity)

    def __str__(self) -> str:
        return f"Mock {self.name}"

    @property
    def additional_info(self) -> str:
        return "Mock info"

    @classmethod
    def create_product(cls, data: dict) -> "MockProduct":
        return cls(**data)


class TestProduct(unittest.TestCase):
    def setUp(self) -> None:
        """Подготовка тестового продукта"""
        self.product = Product("Test Product", "Test Description", 100.0, 10)

    def test_product_implements_base_abstract_methods(self) -> None:
        """Проверка реализации абстрактных методов"""
        self.assertTrue(issubclass(Product, BaseProduct))
        self.assertEqual(self.product.additional_info, "Базовый продукт")

    def test_price_property(self) -> None:
        """Тест свойства price"""
        self.assertEqual(self.product.price, 100.0)
        self.product.price = 150.0
        self.assertEqual(self.product.price, 150.0)

    def test_invalid_price(self) -> None:
        """Тест невалидной цены"""
        with self.assertRaises(ValueError):
            self.product.price = -10.0

    def test_apply_discount(self) -> None:
        """Тест применения скидки"""
        self.product.apply_discount(0.1)  # 10% скидка
        self.assertAlmostEqual(self.product.price, 90.0)

    def test_invalid_discount(self) -> None:
        """Тест невалидной скидки"""
        with self.assertRaises(ValueError):
            self.product.apply_discount(1.1)  # Скидка > 100%
        with self.assertRaises(ValueError):
            self.product.apply_discount(-0.1)  # Отрицательная скидка

    def test_str_representation(self) -> None:
        """Тест строкового представления"""
        self.assertEqual(str(self.product), "Test Product, 100.0 руб. Остаток: 10 шт.")
