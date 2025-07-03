# 🛍️ Интернет-магазин электроники и товаров для дома

Проект реализует систему управления продуктами и категориями для интернет-магазина.

## 🛠 Технологии
- Python 3.10+
- Pytest (для тестирования)
- Mypy (для проверки типов)
- Logging (для логирования)

## 🗂 Структура проекта
Python-Commerce/

├── src/

│ ├── base_product.py # Базовый абстрактный класс продукта

│ ├── product.py # Основной класс продукта

│ ├── smartphone.py # Класс смартфонов

│ ├── lawn_grass.py # Класс газонной травы

│ ├── category.py # Управление категориями

│ ├── base_container.py # Базовый класс контейнеров

│ ├── loaders.py # Загрузка данных из JSON

│ └── logging_mixin.py # Миксин для логирования

├── tests/

│ ├── test_product.py # Тесты продуктов

│ ├── test_category.py # Тесты категорий

│ └── test_loaders.py # Тесты загрузчиков

├── data/ # Примеры данных

│ └── products.json

└── README.md

## 🚀 Быстрый старт

 - Клонируйте репозиторий:
```bash
git clone https://github.com/Anton742-Tu/Python-Commerce.git
cd Python_Commerce
```
 - Установите зависимости:
```bash
pip install -r requirements.txt
```
## 🛠 Разработка

### Перед коммитом выполните:
```bash
mypy src/          # Проверка типов
pytest tests/      # Запуск тестов
black src/         # Форматирование кода
```
## 📚 Основные классы
### Базовый класс продукта 'product'
```
product = Product(
    name="Ноутбук", 
    description="Мощный ноутбук", 
    price=50000.0, 
    quantity=10
)
```
### Управление категориями продуктов 'category'
```
category = Category("Электроника", "Техника для дома")
category.add_product(product)
```
## Работа с JSON
```
# Загрузка категорий из файла
categories = JsonLoader.load_categories("data/products.json")

# Сохранение категорий
JsonLoader.save_categories("output.json", categories)
```
### Пример JSON-файла:
```json
{
  "name": "Электроника",
  "description": "Техника для дома",
  "products": [
    {
      "name": "Смартфон",
      "description": "Новый флагман",
      "price": 999.99,
      "quantity": 5
    }
  ]
}
```
## 🧪 Тестирование
### Запуск всех тестов:
```bash
pytest tests/ -v
```
## Проверка покрытия:
```bash
pytest --cov=src tests/
```
## 📝 Лицензия
MIT License. См. файл LICENSE.
