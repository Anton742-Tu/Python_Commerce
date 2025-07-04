import unittest
from src.product import Product


class TestProduct(unittest.TestCase):
    def setUp(self) -> None:
        """Подготовка тестовых данных"""
        self.product = Product(name="Тестовый продукт", description="Тестовое описание", price=1000.0, quantity=10)

    def test_product_initialization(self) -> None:
        """Тест инициализации продукта"""
        self.assertEqual(self.product.name, "Тестовый продукт")
        self.assertEqual(self.product.description, "Тестовое описание")
        self.assertEqual(self.product.price, 1000.0)
        self.assertEqual(self.product.quantity, 10)

    def test_product_str(self) -> None:
        """Тест строкового представления"""
        expected_str = "Тестовый продукт, 1000.0 руб. Остаток: 10 шт."
        self.assertEqual(str(self.product), expected_str)

    def test_additional_info(self) -> None:
        """Тест дополнительной информации"""
        self.assertEqual(self.product.additional_info, "Базовый продукт")

    def test_apply_discount(self) -> None:
        """Тест применения скидки"""
        self.product.apply_discount(0.1)  # 10% скидка
        self.assertAlmostEqual(self.product.price, 900.0, places=2)


if __name__ == "__main__":
    unittest.main()
