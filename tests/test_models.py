import unittest
from models.product import Product
from models.category import Category


class TestProduct(unittest.TestCase):
    """Тесты для класса Product"""

    def test_product_initialization(self) -> None:
        """Проверка инициализации продукта"""
        product = Product(name="Тестовый продукт", description="Тестовое описание", price=1000.0, quantity=10)

        self.assertEqual(product.name, "Тестовый продукт")
        self.assertEqual(product.description, "Тестовое описание")
        self.assertEqual(product.price, 1000.0)
        self.assertEqual(product.quantity, 10)

    def test_product_str(self) -> None:
        """Проверка строкового представления"""
        product = Product("Продукт", "Описание", 500.0, 2)
        self.assertEqual(str(product), "Продукт, 500.0 руб. (Осталось: 2)")


class TestCategory(unittest.TestCase):
    """Тесты для класса Category"""

    def setUp(self) -> None:
        """Подготовка тестовых данных"""
        Category.reset_counters()
        self.test_product1 = Product("Продукт 1", "Описание 1", 100.0, 5)
        self.test_product2 = Product("Продукт 2", "Описание 2", 200.0, 3)
        self.test_category = Category(
            name="Тестовая категория", description="Тестовое описание", products=[self.test_product1]
        )

    def test_category_initialization(self) -> None:
        """Проверка инициализации категории"""
        self.assertEqual(self.test_category.name, "Тестовая категория")
        self.assertEqual(self.test_category.description, "Тестовое описание")
        self.assertEqual(len(self.test_category.products), 1)
        self.assertEqual(self.test_category.products[0].name, "Продукт 1")

    def test_category_count(self) -> None:
        """Проверка подсчета категорий"""
        self.assertEqual(Category._category_count, 1)
        Category("Другая категория", "Описание")
        self.assertEqual(Category._category_count, 2)

    def test_product_count(self) -> None:
        """Проверка подсчета продуктов"""
        self.assertEqual(Category._product_count, 1)
        self.test_category.add_product(self.test_product2)
        self.assertEqual(Category._product_count, 2)

    def test_category_str(self) -> None:
        """Проверка строкового представления"""
        self.assertEqual(str(self.test_category), "Тестовая категория, количество продуктов: 1 шт.")

    def test_add_product(self) -> None:
        """Проверка добавления продукта"""
        initial_count = len(self.test_category.products)
        self.test_category.add_product(self.test_product2)
        self.assertEqual(len(self.test_category.products), initial_count + 1)
        self.assertIn(self.test_product2, self.test_category.products)


if __name__ == "__main__":
    unittest.main()
