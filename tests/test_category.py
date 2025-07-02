import unittest
import pytest

from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass
from src.category import Category


class TestCategoryProducts(unittest.TestCase):
    def setUp(self):
        """Инициализация тестовых данных"""
        Category.reset_counters()  # Сбрасываем счетчики перед каждым тестом
        self.category = Category("Тест", "Описание")
        self.phone = Smartphone("Phone", "Desc", 1000, 2, 2.5, "X", 128, "Black")
        self.grass = LawnGrass("Grass", "Desc", 500, 10, "Russia", 14, "Green")
        self.product = Product("Product", "Desc", 100, 5)

    def test_add_valid_product(self):
        """Тест добавления валидного продукта"""
        initial_count = len(self.category.products)
        self.category.add_product(self.phone)
        self.assertEqual(len(self.category.products), initial_count + 1)
        self.assertIn(self.phone, self.category.products)

    def test_add_invalid_type(self):
        """Тест добавления не-продукта"""
        with self.assertRaises(TypeError) as context:
            self.category.add_product("не продукт")
        self.assertIn("можно добавлять только объекты класса Product", str(context.exception))

    def test_add_multiple_allowed_types(self):
        """Тест добавления нескольких разрешённых типов"""
        # Разрешаем и смартфоны и траву
        self.category.add_product(self.phone, allowed_types=[Smartphone, LawnGrass])
        self.category.add_product(self.grass, allowed_types=[Smartphone, LawnGrass])
        self.assertEqual(len(self.category.products), 2)
        self.assertIsInstance(self.category.products[0], Smartphone)
        self.assertIsInstance(self.category.products[1], LawnGrass)

    def test_category_counters(self):
        """Тест счетчиков категорий и продуктов"""
        Category.reset_counters()

        p1 = Product("Товар1", "Описание", 100, 5)
        p2 = Product("Товар2", "Описание", 200, 3)

        Category("Категория1", "Описание", [p1])
        Category("Категория2", "Описание", [p2])

        self.assertEqual(Category.get_category_count(), 2)
        self.assertEqual(Category.get_product_count(), 2)

    def test_type_based_restrictions(self):
        """Тест ограничений по типам продуктов"""
        category = Category("Тест", "Категория")

        # Проверка базового ограничения
        with pytest.raises(TypeError) as e:
            category.add_product("not a product")
        assert "можно добавлять только объекты класса Product" in str(e.value)

        # Проверка ограничения по конкретному типу
        category.add_product(self.phone, allowed_types=[Smartphone])

        with pytest.raises(TypeError) as e:
            category.add_product(self.grass, allowed_types=[Smartphone])
        assert "Smartphone" in str(e.value)
        assert "LawnGrass" in str(e.value)

    def test_add_product_with_zero_quantity(self):
        """Тест добавления продукта с нулевым количеством"""
        zero_product = Product("Zero", "Desc", 100, 0)
        self.category.add_product(zero_product)
        self.assertIn(zero_product, self.category.products)

    def test_product_str_representation(self):
        """Тест строкового представления продукта в категории"""
        self.category.add_product(self.product)
        products_str = self.category.products
        self.assertIn(self.product.name, products_str)
        self.assertIn(str(self.product.price), products_str)
        self.assertIn(str(self.product.quantity), products_str)

    def test_duplicate_product_addition(self):
        """Тест добавления дубликата продукта"""
        self.category.add_product(self.product)
        initial_count = len(self.category.products)
        self.category.add_product(self.product)  # Добавляем тот же продукт
        self.assertEqual(len(self.category.products), initial_count + 1)


if __name__ == "__main__":
    unittest.main()
