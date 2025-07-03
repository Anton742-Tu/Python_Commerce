import unittest
import os
import json
from tempfile import NamedTemporaryFile
from unittest.mock import patch
from src.loaders import JsonLoader


class TestJsonLoader(unittest.TestCase):
    def setUp(self) -> None:
        """Подготовка тестовых данных"""
        self.test_data = [
            {
                "name": "Smartphones",
                "description": "Mobile devices",
                "products": [{"name": "iPhone 15", "description": "Flagship", "price": 999.99, "quantity": 10}],
            }
        ]

        self.temp_file = NamedTemporaryFile(mode="w+", encoding="utf-8", delete=False, suffix=".json")
        json.dump(self.test_data, self.temp_file, ensure_ascii=False, indent=2)
        self.temp_file.close()

    def tearDown(self) -> None:
        """Удаление временного файла"""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)

    def test_file_not_found(self) -> None:
        """Тест обработки отсутствующего файла"""
        with self.assertRaises(FileNotFoundError):
            JsonLoader.load_categories("nonexistent_file.json")

    def test_invalid_json(self) -> None:
        """Тест обработки невалидного JSON"""
        with open(self.temp_file.name, "w", encoding="utf-8") as f:
            f.write("{invalid json}")

        with self.assertRaises(json.JSONDecodeError):
            JsonLoader.load_categories(self.temp_file.name)

    def test_missing_required_field(self) -> None:
        """Тест отсутствия обязательного поля"""
        invalid_data = [{"description": "No name", "products": []}]
        with open(self.temp_file.name, "w", encoding="utf-8") as f:
            json.dump(invalid_data, f)

        with self.assertRaises(ValueError) as context:
            JsonLoader.load_categories(self.temp_file.name)
        self.assertIn("Отсутствует обязательное поле", str(context.exception))

    def test_file_permission_error(self) -> None:
        """Тест ошибки доступа к файлу"""
        with patch("builtins.open", side_effect=PermissionError("Access denied")):
            with self.assertRaises(PermissionError):
                JsonLoader.load_categories("any_file.json")


if __name__ == "__main__":
    unittest.main()
