import json
from pathlib import Path
from typing import List
from src.product import Product
from src.category import Category


class DataLoader:
    @staticmethod
    def load_categories_from_json(file_path: str | Path) -> List[Category]:
        """
        Загружает категории из JSON файла
        :param file_path: Путь к JSON файлу
        :return: Список объектов Category
        :raises FileNotFoundError: Если файл не найден
        :raises json.JSONDecodeError: При ошибке парсинга JSON
        :raises ValueError: При неверной структуре данных
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise ValueError("JSON должен содержать список категорий")

            return [
                Category(
                    name=str(category_data["name"]),
                    description=str(category_data["description"]),
                    products=[
                        Product(
                            name=str(product["name"]),
                            description=str(product["description"]),
                            price=float(product["price"]),
                            quantity=int(product["quantity"]),
                        )
                        for product in category_data.get("products", [])
                    ],
                )
                for category_data in data
            ]

        except FileNotFoundError as e:
            raise FileNotFoundError(f"Файл {file_path} не найден") from e
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Ошибка декодирования JSON в файле {file_path}", e.doc, e.pos) from e
        except KeyError as e:
            raise ValueError(f"Отсутствует обязательное поле: {e}") from e

    @staticmethod
    def save_categories_to_json(file_path: str | Path, categories: List[Category]) -> None:
        """
        Сохраняет категории в JSON файл
        :param file_path: Путь для сохранения
        :param categories: Список категорий для сохранения
        """
        output_data = []

        for category in categories:
            category_dict = {"name": category.name, "description": category.description, "products": []}

            # Получаем продукты через защищенный атрибут (если есть доступ)
            # Или через дополнительный метод в классе Category
            if hasattr(category, "_Category__products"):
                products = getattr(category, "_Category__products")
                for product in products:
                    category_dict["products"].append(  # type: ignore
                        {
                            "name": product.name,
                            "description": product.description,
                            "price": product.price,
                            "quantity": product.quantity,
                        }
                    )

            output_data.append(category_dict)

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(output_data, file, ensure_ascii=False, indent=4)
