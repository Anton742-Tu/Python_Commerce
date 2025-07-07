from src.category import Category
from src.product import Product

if __name__ == "__main__":
    # Тестирование обработки нулевого количества
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(f"Ошибка при создании продукта: {e}")
    else:
        print("Ошибка не возникла - это неверное поведение!")

    # Создаем корректные продукты
    try:
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    except ValueError as e:
        print(f"Ошибка при создании продуктов: {e}")
        exit(1)

    # Создаем категорию и добавляем продукты
    try:
        category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])
        print(f"Средняя цена в категории '{category1.name}': {category1.get_average_price():.2f} руб.")

        # Выводим информацию о товарах
        for product in category1.products:
            print(f"  - {product}")
    except Exception as e:
        print(f"Ошибка при работе с категорией: {e}")

    # Тестирование пустой категории
    try:
        category_empty = Category("Пустая категория", "Категория без продуктов")
        print(f"\nСредняя цена в пустой категории: {category_empty.get_average_price():.2f} руб.")
    except Exception as e:
        print(f"Ошибка при работе с пустой категорией: {e}")
