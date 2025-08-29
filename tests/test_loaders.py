import json
import os
from tempfile import NamedTemporaryFile
from typing import List, Dict, Any
from unittest import TestCase, mock
from src.loaders import JsonLoader
from src.category import Category


class TestJsonLoader(TestCase):
    def setUp(self) -> None:
        """Подготовка тестовых данных"""
        self.test_data: List[Dict[str, Any]] = [
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

    def test_missing_required_field(self) -> None:
        """Тест отсутствия обязательного поля"""
        invalid_data: List[Dict[str, Any]] = [{"description": "No name", "products": []}]
        with open(self.temp_file.name, "w", encoding="utf-8") as f:
            json.dump(invalid_data, f)

        with self.assertRaises(ValueError) as context:
            JsonLoader.load_categories(self.temp_file.name)
        self.assertIn("Отсутствуют обязательные поля 'name' или 'description'", str(context.exception))

    def test_file_permission_error(self) -> None:
        """Тест ошибки доступа к файлу"""
        with mock.patch("builtins.open", side_effect=PermissionError("Access denied")):
            with self.assertRaises(PermissionError):
                JsonLoader.load_categories("any_file.json")

    def test_load_valid_data(self) -> None:
        """Тест загрузки валидных данных"""
        categories: List[Category] = JsonLoader.load_categories(self.temp_file.name)
        self.assertEqual(len(categories), 1)
        self.assertEqual(categories[0].name, "Smartphones")
