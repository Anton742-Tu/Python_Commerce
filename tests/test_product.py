import unittest
from decimal import Decimal

from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


class TestProduct(unittest.TestCase):
    def setUp(self):
        """Подготовка тестовых данных"""
        self.product_data = {
            "name": "Тестовый продукт",
            "description": "Тестовое описание",
            "price": 1000.0,
            "quantity": 10,
        }

    def test_product_initialization(self) -> None:
        """Тест инициализации продукта"""
        product = Product(**self.product_data)

        self.assertEqual(product.name, self.product_data["name"])
        self.assertEqual(product.description, self.product_data["description"])
        self.assertEqual(float(product.price), self.product_data["price"])
        self.assertEqual(product.quantity, self.product_data["quantity"])

    def test_product_str(self) -> None:
        """Тест строкового представления"""
        product = Product(**self.product_data)
        expected_str = (f"{self.product_data['name']}, "
                        f"{self.product_data['price']} руб. Остаток: {self.product_data['quantity']} шт.")
        self.assertEqual(str(product), expected_str)

    def test_price_setter_validation(self):
        """Тест валидации цены"""
        product = Product(**self.product_data)

        with self.assertRaises(ValueError):
            product.price = -100

        with self.assertRaises(ValueError):
            product.price = 0

    def test_quantity_setter_validation(self):
        """Тест валидации количества"""
        product = Product(**self.product_data)

        with self.assertRaises(ValueError):
            product.quantity = -5

    def test_apply_discount(self):
        """Тест применения скидки"""
        product = Product(**self.product_data)
        original_price = product.price

        # Применяем скидку 10%
        product.apply_discount(0.1)
        self.assertEqual(product.price, Decimal(str(original_price * 0.9)))

        # Проверка на недопустимые значения скидки
        with self.assertRaises(ValueError):
            product.apply_discount(1.1)
        with self.assertRaises(ValueError):
            product.apply_discount(-0.1)


class TestSmartphone(unittest.TestCase):
    def setUp(self):
        self.phone_data = {
            "name": "iPhone 15",
            "description": "Flagship",
            "price": 999.99,
            "quantity": 5,
            "performance": 3.2,
            "model": "Pro",
            "memory": 256,
            "color": "Black",
        }

    def test_smartphone_creation(self):
        """Тест создания смартфона"""
        phone = Smartphone(**self.phone_data)

        self.assertEqual(phone.model, self.phone_data["model"])
        self.assertEqual(phone.memory, self.phone_data["memory"])
        self.assertEqual(phone.color, self.phone_data["color"])
        self.assertEqual(phone.performance, self.phone_data["performance"])

    def test_smartphone_additional_info(self):
        """Тест дополнительной информации смартфона"""
        phone = Smartphone(**self.phone_data)
        info = phone.additional_info
        self.assertIn(self.phone_data["model"], info)
        self.assertIn(str(self.phone_data["memory"]), info)
        self.assertIn(self.phone_data["color"], info)

    def test_smartphone_inheritance(self):
        """Тест наследования от Product"""
        phone = Smartphone(**self.phone_data)
        self.assertIsInstance(phone, Product)


class TestLawnGrass(unittest.TestCase):
    def setUp(self):
        self.grass_data = {
            "name": "Premium Grass",
            "description": "High quality",
            "price": 49.99,
            "quantity": 100,
            "country": "Netherlands",
            "germination_period": 14,
            "color": "Emerald Green",
        }

    def test_lawn_grass_creation(self):
        """Тест создания газонной травы"""
        grass = LawnGrass(**self.grass_data)

        self.assertEqual(grass.country, self.grass_data["country"])
        self.assertEqual(grass.germination_period, self.grass_data["germination_period"])
        self.assertEqual(grass.color, self.grass_data["color"])

    def test_lawn_grass_additional_info(self):
        """Тест дополнительной информации газонной травы"""
        grass = LawnGrass(**self.grass_data)
        info = grass.additional_info
        self.assertIn(self.grass_data["country"], info)
        self.assertIn(str(self.grass_data["germination_period"]), info)
        self.assertIn(self.grass_data["color"], info)

    def test_lawn_grass_inheritance(self):
        """Тест наследования от Product"""
        grass = LawnGrass(**self.grass_data)
        self.assertIsInstance(grass, Product)


class TestProductAddition(unittest.TestCase):
    def setUp(self):
        self.phone1 = Smartphone("Phone1", "Desc", 1000, 2, 2.5, "X", 128, "Black")
        self.phone2 = Smartphone("Phone2", "Desc", 2000, 3, 3.0, "Y", 256, "White")
        self.grass1 = LawnGrass("Grass1", "Desc", 500, 10, "Russia", 14, "Green")
        self.grass2 = LawnGrass("Grass2", "Desc", 700, 5, "USA", 10, "Blue")

    def test_valid_addition(self):
        """Тест сложения продуктов одного класса"""
        # Сложение смартфонов
        self.assertEqual(self.phone1 + self.phone2, 1000 * 2 + 2000 * 3)

        # Сложение газонных трав
        self.assertEqual(self.grass1 + self.grass2, 500 * 10 + 700 * 5)

    def test_invalid_addition(self):
        """Тест попытки сложения разных классов"""
        with self.assertRaises(TypeError):
            _ = self.phone1 + self.grass1

        with self.assertRaises(TypeError):
            _ = self.grass2 + self.phone2

    def test_addition_with_zero_quantity(self):
        """Тест сложения с нулевым количеством"""
        phone3 = Smartphone("Phone3", "Desc", 1500, 0, 2.5, "Z", 128, "Red")
        self.assertEqual(self.phone1 + phone3, 1000 * 2 + 1500 * 0)


if __name__ == "__main__":
    unittest.main()
