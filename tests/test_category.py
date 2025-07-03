import unittest
from src.category import Category
from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


class TestCategory(unittest.TestCase):
    def setUp(self) -> None:
        """Подготовка тестовых данных"""
        self.category = Category("Тест", "Описание")
        self.valid_product = Product(name="Тестовый товар", description="Тестовое описание", price=100.0, quantity=5)
        self.phone = Smartphone(
            name="Смартфон",
            description="Описание",
            price=1000.0,
            quantity=2,
            performance=2.5,
            model="X",
            memory=128,
            color="Black",
        )
        self.grass = LawnGrass(
            name="Трава",
            description="Описание",
            price=500.0,
            quantity=10,
            country="Россия",
            germination_period=14,
            color="Зеленый",
        )

    def test_add_valid_product(self) -> None:
        """Тест добавления валидного продукта"""
        initial_count = len(self.category.products)
        self.category.add_product(self.valid_product)
        self.assertEqual(len(self.category.products), initial_count + 1)

    def test_add_multiple_allowed_types(self) -> None:
        """Тест добавления нескольких разрешённых типов"""
        self.category.add_product(self.phone, allowed_types=[Smartphone, LawnGrass])
        self.category.add_product(self.grass, allowed_types=[Smartphone, LawnGrass])
        self.assertEqual(len(self.category.products), 2)

    def test_type_based_restrictions(self) -> None:
        """Тест ограничений по типам продуктов"""
        category = Category("Тест", "Категория")

        # Проверка ограничения по конкретному типу
        category.add_product(self.phone, allowed_types=[Smartphone])

        with self.assertRaises(TypeError):
            category.add_product(self.grass, allowed_types=[Smartphone])


if __name__ == "__main__":
    unittest.main()
