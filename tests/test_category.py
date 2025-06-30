import unittest

from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass
from src.category import Category


class TestCategoryProducts(unittest.TestCase):
    def setUp(self):
        self.category = Category("Тест", "Описание")
        self.phone = Smartphone("Phone", "Desc", 1000, 2, 2.5, "X", 128, "Black")
        self.grass = LawnGrass("Grass", "Desc", 500, 10, "Russia", 14, "Green")

    def test_add_valid_product(self):
        """Тест добавления валидного продукта"""
        initial_count = len(self.category._Category__products)
        self.category.add_product(self.phone)
        self.assertEqual(len(self.category._Category__products), initial_count + 1)

    def test_add_invalid_type(self):
        """Тест добавления не-продукта"""
        with self.assertRaises(TypeError):
            self.category.add_product("не продукт")

    def test_add_restricted_type(self):
        """Тест ограничения типов продуктов"""
        # Разрешаем только смартфоны
        self.category.add_product(self.phone, allowed_types=[Smartphone])

        with self.assertRaises(TypeError) as context:
            self.category.add_product(self.grass, allowed_types=[Smartphone])
        self.assertIn("Разрешены только продукты типов: Smartphone", str(context.exception))

    def test_add_multiple_allowed_types(self):
        """Тест добавления нескольких разрешённых типов"""
        # Разрешаем и смартфоны и траву
        self.category.add_product(self.phone, allowed_types=[Smartphone, LawnGrass])
        self.category.add_product(self.grass, allowed_types=[Smartphone, LawnGrass])
        self.assertEqual(len(self.category._Category__products), 2)


def test_category_counters():
    Category.reset_counters()

    p1 = Product("Товар1", "Описание", 100, 5)
    p2 = Product("Товар2", "Описание", 200, 3)

    Category("Категория1", "Описание", [p1])
    Category("Категория2", "Описание", [p2])

    assert Category.get_category_count() == 2
    assert Category.get_product_count() == 2


if __name__ == "__main__":
    unittest.main()
