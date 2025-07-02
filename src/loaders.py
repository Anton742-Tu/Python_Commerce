import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from src.category import Category
from src.exceptions.data_errors import InvalidDataError, FileOperationError


class JsonLoader:
    @staticmethod
    def load_categories(file_path: str | Path) -> List[Category]:
        """
        Загружает категории из JSON файла с автоматическим определением кодировки

        Args:
            file_path: Путь к JSON файлу (строка или Path объект)

        Returns:
            Список объектов Category

        Raises:
            FileOperationError: При ошибках работы с файлом
            InvalidDataError: При проблемах с данными
        """
        file_path = Path(file_path)

        if not file_path.exists():
            raise FileOperationError(f"Файл не найден: {file_path}")
        if not file_path.is_file():
            raise FileOperationError(f"Указанный путь не является файлом: {file_path}")

        try:
            # Пытаемся прочитать с разными кодировками
            for encoding in ["utf-8", "cp1251", "ascii"]:
                try:
                    with file_path.open("r", encoding=encoding) as file:
                        data = file.read()
                        return JsonLoader._parse_data(data, str(file_path))
                except UnicodeDecodeError:
                    continue

            raise FileOperationError(f"Не удалось декодировать файл {file_path} с поддерживаемыми кодировками")

        except PermissionError as e:
            raise FileOperationError(f"Нет прав на чтение файла: {file_path}") from e

    @staticmethod
    def _parse_data(json_str: str, source: str) -> List[Category]:
        """
        Парсит JSON строку в список категорий

        Args:
            json_str: Строка с JSON данными
            source: Источник данных (для сообщений об ошибках)

        Returns:
            Список объектов Category

        Raises:
            InvalidDataError: При неверной структуре данных
        """
        try:
            data = json.loads(json_str)

            if not isinstance(data, list):
                raise InvalidDataError(f"Ожидается список категорий, получен {type(data).__name__}")

            categories = []
            for idx, item in enumerate(data, 1):
                try:
                    categories.append(Category.from_dict(item))
                except (KeyError, ValueError, TypeError) as e:
                    raise InvalidDataError(f"Ошибка в элементе {idx} из {source}: {str(e)}") from e

            return categories

        except json.JSONDecodeError as e:
            raise InvalidDataError(f"Ошибка JSON в {source} (строка {e.lineno}, колонка {e.colno}): {e.msg}") from e

    @staticmethod
    def save_categories(
        file_path: str | Path, categories: List[Category], indent: Optional[int] = 2, ensure_ascii: bool = False
    ) -> None:
        """
        Сохраняет категории в JSON файл

        Args:
            file_path: Путь для сохранения
            categories: Список категорий для сохранения
            indent: Отступ для форматирования (None - без форматирования)
            ensure_ascii: Экранировать не-ASCII символы

        Raises:
            FileOperationError: При ошибках записи
        """
        file_path = Path(file_path)

        try:
            data = JsonLoader._prepare_export_data(categories)

            with file_path.open("w", encoding="utf-8") as file:
                json.dump(data, file, indent=indent, ensure_ascii=ensure_ascii)

        except (PermissionError, IsADirectoryError) as e:
            raise FileOperationError(f"Ошибка записи в файл {file_path}: {str(e)}") from e

    @staticmethod
    def _prepare_export_data(categories: List[Category]) -> List[Dict[str, Any]]:
        """Подготавливает данные категорий для экспорта"""
        return [
            {
                "name": cat.name,
                "description": cat.description,
                "products": [
                    {
                        "name": prod.name,
                        "description": prod.description,
                        "price": float(prod.price),  # Явное преобразование для Decimal
                        "quantity": int(prod.quantity),
                        **getattr(prod, "additional_attributes", {}),
                    }
                    for prod in cat.products
                ],
            }
            for cat in categories
        ]
