import unittest
from unittest.mock import patch

from src.product import Product
from src.category import Category
from typing import Any


class TestProduct(unittest.TestCase):
    def test_product_initialization(self) -> None:
        """Тест инициализации продукта"""
        product = Product(name="Тестовый продукт", description="Тестовое описание", price=1000.0, quantity=10)

        self.assertEqual(product.name, "Тестовый продукт")
        self.assertEqual(product.description, "Тестовое описание")
        self.assertEqual(product.price, 1000.0)
        self.assertEqual(product.quantity, 10)

    def test_product_str(self) -> None:
        """Тест строкового представления"""
        product = Product("Продукт", "Описание", 500.0, 2)
        self.assertEqual(str(product), "Продукт, 500.0 руб. Остаток: 2 шт.")


class TestCategory(unittest.TestCase):
    def setUp(self) -> None:
        """Подготовка тестовых данных"""
        Category.reset_counters()
        self.test_product1 = Product("Продукт 1", "Описание 1", 100.0, 5)
        self.test_product2 = Product("Продукт 2", "Описание 2", 200.0, 3)
        self.test_category = Category(
            name="Тестовая категория", description="Тестовое описание", products=[self.test_product1]
        )

    def test_category_initialization(self) -> None:
        """Тест инициализации категории"""
        self.assertEqual(self.test_category.name, "Тестовая категория")
        self.assertEqual(self.test_category.description, "Тестовое описание")
        self.assertEqual(len(self.test_category.products.split("\n")), 1)

    def test_category_count(self) -> None:
        """Тест подсчета категорий"""
        self.assertEqual(Category.get_total_categories(), 1)
        Category("Другая категория", "Описание")
        self.assertEqual(Category.get_total_categories(), 2)

    def test_product_count(self) -> None:
        """Тест подсчета продуктов"""
        self.assertEqual(Category.get_total_products(), 1)
        self.test_category.add_product(self.test_product2)
        self.assertEqual(Category.get_total_products(), 2)

    def test_category_str(self) -> None:
        """Тест строкового представления"""
        self.assertEqual(str(self.test_category), "Тестовая категория, количество продуктов: 1 шт.")

    @patch("builtins.print")
    def test_add_invalid_product(self, mock_print: Any) -> None:
        """Тест добавления невалидного продукта"""
        with self.assertRaises(TypeError):
            self.test_category.add_product("not a product")  # type: ignore
        mock_print.assert_not_called()


if __name__ == "__main__":
    unittest.main()
