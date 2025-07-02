import unittest
import os
import json
from tempfile import mkdtemp
from unittest.mock import patch
from pathlib import Path

from src.loaders import JsonLoader
from src.exceptions.data_errors import FileOperationError, InvalidDataError


class TestJsonLoader(unittest.TestCase):
    def setUp(self) -> None:
        """Подготовка тестовых данных"""
        self.test_data = [
            {
                "name": "Smartphones",
                "description": "Mobile devices",
                "products": [
                    {
                        "name": "iPhone 15",
                        "description": "Flagship",
                        "price": 999.99,
                        "quantity": 10,
                        "color": "Black",  # Дополнительное поле
                    }
                ],
            }
        ]

        # Создаем временный файл с корректными данными
        self.temp_dir = mkdtemp()
        self.valid_file = os.path.join(self.temp_dir, "valid.json")
        with open(self.valid_file, "w", encoding="utf-8") as f:
            json.dump(self.test_data, f, ensure_ascii=False, indent=2)

        # Создаем файл с неверной кодировкой (cp1251)
        self.win1251_file = os.path.join(self.temp_dir, "win1251.json")
        with open(self.win1251_file, "w", encoding="cp1251") as f:
            json.dump(self.test_data, f, ensure_ascii=False, indent=2)

    def tearDown(self) -> None:
        """Удаление временных файлов"""
        for f in [self.valid_file, self.win1251_file]:
            if os.path.exists(f):
                os.unlink(f)
        os.rmdir(self.temp_dir)

    def test_load_valid_data(self) -> None:
        """Тест загрузки валидного JSON файла"""
        categories = JsonLoader.load_categories(self.valid_file)
        self.assertEqual(len(categories), 1)
        self.assertEqual(categories[0].name, "Smartphones")
        self.assertEqual(len(categories[0].products), 1)
        self.assertEqual(categories[0].products[0].name, "iPhone 15")

    def test_file_not_found(self) -> None:
        """Тест обработки отсутствующего файла"""
        with self.assertRaises(FileOperationError):
            JsonLoader.load_categories("nonexistent_file.json")

    def test_invalid_json(self) -> None:
        """Тест обработки невалидного JSON"""
        with open(self.valid_file, "w", encoding="utf-8") as f:
            f.write("{invalid json}")

        with self.assertRaises(InvalidDataError) as context:
            JsonLoader.load_categories(self.valid_file)
        self.assertIn("Ошибка JSON", str(context.exception))

    def test_missing_required_field(self) -> None:
        """Тест отсутствия обязательного поля"""
        invalid_data = [{"description": "No name", "products": []}]
        with open(self.valid_file, "w", encoding="utf-8") as f:
            json.dump(invalid_data, f)

        with self.assertRaises(InvalidDataError) as context:
            JsonLoader.load_categories(self.valid_file)
        self.assertIn("Отсутствует обязательное поле", str(context.exception))

    def test_empty_products_list(self) -> None:
        """Тест пустого списка продуктов"""
        test_data = [{"name": "Empty", "description": "No products", "products": []}]
        with open(self.valid_file, "w", encoding="utf-8") as f:
            json.dump(test_data, f)

        categories = JsonLoader.load_categories(self.valid_file)
        self.assertEqual(len(categories), 1)
        self.assertEqual(len(categories[0].products), 0)

    def test_file_permission_error(self) -> None:
        """Тест ошибки доступа к файлу"""
        with patch("builtins.open", side_effect=PermissionError("Access denied")):
            with self.assertRaises(FileOperationError):
                JsonLoader.load_categories("any_file.json")

    def test_alternative_encoding(self) -> None:
        """Тест загрузки файла с альтернативной кодировкой"""
        categories = JsonLoader.load_categories(self.win1251_file)
        self.assertEqual(len(categories), 1)

    def test_save_and_load_roundtrip(self) -> None:
        """Тест сохранения и последующей загрузки"""
        # Загружаем исходные данные
        categories = JsonLoader.load_categories(self.valid_file)

        # Сохраняем во временный файл
        temp_save = os.path.join(self.temp_dir, "saved.json")
        JsonLoader.save_categories(temp_save, categories)

        # Загружаем обратно и проверяем
        loaded = JsonLoader.load_categories(temp_save)
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].name, "Smartphones")
        self.assertEqual(len(loaded[0].products), 1)

    def test_save_empty_categories(self) -> None:
        """Тест сохранения пустого списка категорий"""
        temp_save = os.path.join(self.temp_dir, "empty.json")
        JsonLoader.save_categories(temp_save, [])

        with open(temp_save, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.assertEqual(data, [])

    def test_pathlib_support(self) -> None:
        """Тест поддержки Path объектов"""
        path = Path(self.valid_file)
        categories = JsonLoader.load_categories(path)
        self.assertEqual(len(categories), 1)

    def test_additional_product_fields(self) -> None:
        """Тест сохранения дополнительных полей продукта"""
        categories = JsonLoader.load_categories(self.valid_file)
        temp_save = os.path.join(self.temp_dir, "with_fields.json")
        JsonLoader.save_categories(temp_save, categories)

        with open(temp_save, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.assertIn("color", data[0]["products"][0])


if __name__ == "__main__":
    unittest.main()
