import json
from pathlib import Path
from typing import List
from category import Category


class DataLoader:
    @staticmethod
    def load_categories_from_json(file_path: str | Path) -> List[Category]:
        """
        Загружает категории и товары из JSON файла
        :param file_path: Путь к JSON файлу
        :return: Список категорий с товарами
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            return [Category.from_dict(category_data) for category_data in data]
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {file_path} не найден")
        except json.JSONDecodeError:
            raise ValueError(f"Файл {file_path} содержит невалидный JSON")

    @staticmethod
    def save_categories_to_json(file_path: str | Path, categories: List[Category]) -> None:
        """
        Сохраняет категории в JSON файл
        :param file_path: Путь для сохранения
        :param categories: Список категорий
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
                        "quantity": prod.quantity
                    }
                    for prod in cat.products
                ]
            }
            for cat in categories
        ]

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
