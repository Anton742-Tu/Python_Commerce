import unittest
import os
import json
from tempfile import NamedTemporaryFile
from models.category import Category


class TestJsonLoader(unittest.TestCase):
    def setUp(self):
        # Создаем временный JSON файл для тестов
        self.test_data = [
            {
                "name": "Тестовая категория",
                "description": "Описание",
                "products": [
                    {
                        "name": "Тестовый продукт",
                        "description": "Описание",
                        "price": 1000.0,
                        "quantity": 10
                    }
                ]
            }
        ]
        self.temp_file = NamedTemporaryFile(mode='w+', delete=False, suffix='.json')
        json.dump(self.test_data, self.temp_file)
        self.temp_file.close()

    def tearDown(self):
        os.unlink(self.temp_file.name)

    def test_load_from_json(self):
        """Тест загрузки из JSON файла"""
        categories = Category.load_from_json(self.temp_file.name)
        self.assertEqual(len(categories), 1)
        self.assertEqual(categories[0].name, "Тестовая категория")
        self.assertEqual(len(categories[0].products), 1)
        self.assertEqual(categories[0].products[0].name, "Тестовый продукт")

    def test_file_not_found(self):
        """Тест обработки отсутствующего файла"""
        with self.assertRaises(FileNotFoundError):
            Category.load_from_json("nonexistent_file.json")

    def test_invalid_json(self):
        """Тест обработки невалидного JSON"""
        with open(self.temp_file.name, 'w') as f:
            f.write("invalid json")

        with self.assertRaises(json.JSONDecodeError):
            Category.load_from_json(self.temp_file.name)


if __name__ == "__main__":
    unittest.main()
