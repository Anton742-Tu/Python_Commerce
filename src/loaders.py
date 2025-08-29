import json
from pathlib import Path
from typing import List
from src.category import Category


class JsonLoader:
    @staticmethod
    def load_categories(file_path: str | Path) -> List[Category]:
        """
        Загружает категории из JSON файла
        :param file_path: Путь к JSON файлу
        :return: Список категорий
        :raises FileNotFoundError: Если файл не найден
        :raises json.JSONDecodeError: При ошибке парсинга JSON
        :raises ValueError: При неверной структуре данных
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = file.read()
                return JsonLoader._parse_data(data, str(file_path))
        except UnicodeDecodeError:
            with open(file_path, "r", encoding="cp1251") as file:
                data = file.read()
                return JsonLoader._parse_data(data, str(file_path))

    @staticmethod
    def _parse_data(json_str: str, file_path: str) -> List[Category]:
        """Внутренний метод для парсинга JSON строки"""
        try:
            data = json.loads(json_str)
            if not isinstance(data, list):
                raise ValueError(f"Файл {file_path} должен содержать список категорий")

            categories = []
            for item in data:
                try:
                    categories.append(Category.from_dict(item))
                except ValueError as e:
                    raise ValueError(f"Ошибка в данных из {file_path}: {str(e)}")

            return categories

        except json.JSONDecodeError as e:
            raise ValueError(f"Ошибка JSON в файле {file_path}: {str(e)}")


def save_categories(file_path: str | Path, categories: List[Category]) -> None:
    """Save categories to JSON file

    Args:
        file_path: Path to save file
        categories: List of categories to save
    """
    data = [
        {
            "name": cat.name,
            "description": cat.description,
            "products": [
                {
                    "name": prod.name,
                    "description": prod.description,
                    "price": prod.price,
                    "quantity": prod.quantity,
                }
                for prod in cat.products  # Используем публичное свойство products
            ],
        }
        for cat in categories
    ]

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
