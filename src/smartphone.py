from src.product import Product
from typing import Dict, Any


class Smartphone(Product):
    """Класс для смартфонов, наследующий от Product"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        performance: float,
        model: str,
        memory: int,
        color: str,
        **kwargs: Any,
    ) -> None:
        """
        Инициализация смартфона

        Args:
            name: Название
            description: Описание
            price: Цена
            quantity: Количество
            performance: Производительность (GHz)
            model: Модель
            memory: Объем памяти (GB)
            color: Цвет
            kwargs: Дополнительные параметры
        """
        super().__init__(name=name, description=description, price=price, quantity=quantity, **kwargs)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    @property
    def additional_info(self) -> str:
        """Дополнительная информация о смартфоне"""
        return (
            f"Модель: {self.model}, Цвет: {self.color}, "
            f"Производительность: {self.performance} GHz, Память: {self.memory}GB"
        )

    def __str__(self) -> str:
        """Строковое представление смартфона"""
        base_info = super().__str__()
        return f"{base_info}\n{self.additional_info}"

    @classmethod
    def create_product(cls, data: Dict[str, Any]) -> "Smartphone":
        """Создание смартфона из словаря"""
        return cls(
            name=str(data["name"]),
            description=str(data["description"]),
            price=float(data["price"]),
            quantity=int(data["quantity"]),
            performance=float(data.get("performance", 0)),
            model=str(data.get("model", "")),
            memory=int(data.get("memory", 0)),
            color=str(data.get("color", "")),
        )
