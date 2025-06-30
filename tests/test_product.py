import unittest

from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


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


class TestProducts(unittest.TestCase):
    def test_smartphone_creation(self):
        phone = Smartphone("Phone", "Desc", 1000, 5, 2.5, "X", 128, "Black")
        self.assertEqual(phone.model, "X")
        self.assertEqual(phone.memory, 128)

    def test_lawn_grass_creation(self):
        grass = LawnGrass("Grass", "Desc", 200, 10, "Russia", 10, "Green")
        self.assertEqual(grass.country, "Russia")
        self.assertEqual(grass.germination_period, 10)

    def test_inheritance(self):
        phone = Smartphone("Phone", "Desc", 1000, 5, 2.5, "X", 128, "Black")
        grass = LawnGrass("Grass", "Desc", 200, 10, "Russia", 10, "Green")
        self.assertIsInstance(phone, Product)
        self.assertIsInstance(grass, Product)


class TestProductAddition(unittest.TestCase):
    def setUp(self):
        self.phone1 = Smartphone("Phone1", "Desc", 1000, 2, 2.5, "X", 128, "Black")
        self.phone2 = Smartphone("Phone2", "Desc", 2000, 3, 3.0, "Y", 256, "White")
        self.grass1 = LawnGrass("Grass1", "Desc", 500, 10, "Russia", 14, "Green")
        self.grass2 = LawnGrass("Grass2", "Desc", 700, 5, "USA", 10, "Blue")

    def test_valid_addition(self):
        # Сложение смартфонов
        self.assertEqual(self.phone1 + self.phone2, 1000 * 2 + 2000 * 3)

        # Сложение газонных трав
        self.assertEqual(self.grass1 + self.grass2, 500 * 10 + 700 * 5)

    def test_invalid_addition(self):
        # Попытка сложить разные классы
        with self.assertRaises(TypeError):
            self.phone1 + self.grass1

        with self.assertRaises(TypeError):
            self.grass2 + self.phone2


if __name__ == "__main__":
    unittest.main()
