import unittest
from src.category import Category
from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass
from src.exceptions import ZeroQuantityError


class TestCategoryAddProduct(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)

    def setUp(self) -> None:
        self.category = Category("Тест", "Категория")
        self.valid_product = Product("Товар", "Описание", 100.0, 1)
        self.zero_product = Product("Нулевой", "Описание", 100.0, 0)  # Создаем объект, но с quantity=0

    def test_add_zero_quantity_product(self) -> None:
        """Тест добавления товара с нулевым количеством"""
        # Создаем товар с нулевым количеством (но сам объект должен существовать)
        zero_product = Product("Нулевой товар", "Описание", 100.0, 0)

        with self.assertLogs("Category", level="INFO") as cm:
            with self.assertRaises(ZeroQuantityError):
                self.category.add_product(zero_product)

        # Проверяем сообщения в логах
        self.assertIn("Начало добавления товара: Нулевой товар", cm.output[0])
        self.assertIn("Товар с нулевым количеством не может быть добавлен", cm.output[1])


class TestCategory(unittest.TestCase):
    def setUp(self) -> None:
        self.category = Category("Тест", "Категория")
        self.phone = Smartphone("Phone", "Desc", 1000, 1, 2.5, "X", 128, "Black")
        self.grass = LawnGrass("Grass", "Desc", 500, 1, "Russia", 14, "Green")
        self.product = Product("Product", "Desc", 100, 1)

    def test_add_multiple_allowed_types(self) -> None:
        """Тест добавления нескольких разрешённых типов"""
        with self.assertLogs("Category", level="INFO"):
            self.category.add_product(self.phone, allowed_types=[Smartphone, LawnGrass])
            self.category.add_product(self.grass, allowed_types=[Smartphone, LawnGrass])
            self.assertEqual(len(self.category.products), 2)

    def test_average_price_with_valid_products(self) -> None:
        """Тест средней цены с товарами"""
        self.category.add_product(Product("Товар1", "Описание", 100, 2))
        self.category.add_product(Product("Товар2", "Описание", 200, 3))
        with self.assertLogs("Category", level="INFO"):
            self.assertAlmostEqual(self.category.get_average_price(), 160.0)

    def test_average_price_empty_category(self) -> None:
        """Тест пустой категории"""
        with self.assertLogs("Category", level="INFO"):
            self.assertEqual(self.category.get_average_price(), 0.0)


if __name__ == "__main__":
    unittest.main()
