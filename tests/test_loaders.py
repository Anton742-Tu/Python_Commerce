import unittest
import os
import json
from tempfile import NamedTemporaryFile
from src.category import Category


class TestJsonLoader(unittest.TestCase):
    def setUp(self) -> None:
        self.test_data = [
            {
                "name": "Тестовая категория",
                "description": "Описание",
                "products": [{"name": "Тестовый продукт", "description": "Описание", "price": 1000.0, "quantity": 10}],
            }
        ]
        self.temp_file = NamedTemporaryFile(mode="w+", delete=False, suffix=".json")
        json.dump(self.test_data, self.temp_file, ensure_ascii=False, indent=2)
        self.temp_file.close()

    def tearDown(self) -> None:
        os.unlink(self.temp_file.name)

    def test_file_not_found(self) -> None:
        """Тест обработки отсутствующего файла"""
        with self.assertRaises(FileNotFoundError):
            Category.load_from_json("nonexistent_file.json")

    def test_invalid_json(self) -> None:
        """Тест обработки невалидного JSON"""
        with open(self.temp_file.name, "w") as f:
            f.write("{invalid json}")

        with self.assertRaises(json.JSONDecodeError):
            Category.load_from_json(self.temp_file.name)

    def test_missing_required_field(self) -> None:
        """Тест отсутствия обязательного поля"""
        invalid_data = [{"description": "Нет названия", "products": []}]
        with open(self.temp_file.name, "w") as f:
            json.dump(invalid_data, f)

        with self.assertRaises(KeyError):
            Category.load_from_json(self.temp_file.name)

    def test_wrong_data_structure(self) -> None:
        """Тест некорректной структуры данных"""
        with open(self.temp_file.name, "w") as f:
            json.dump({"not_a_list": True}, f)

        with self.assertRaises(ValueError):
            Category.load_from_json(self.temp_file.name)


if __name__ == "__main__":
    unittest.main()
