from typing import Any, Dict

from src.product import Product


class LawnGrass(Product):
    """Класс для газонной травы, наследующий от Product"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
        **kwargs: Any,
    ) -> None:
        """
        Инициализация газонной травы

        Args:
            name: Название
            description: Описание
            price: Цена
            quantity: Количество
            country: Страна-производитель
            germination_period: Срок прорастания (дни)
            color: Цвет
            kwargs: Дополнительные параметры
        """
        super().__init__(name=name, description=description, price=price, quantity=quantity, **kwargs)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    @property
    def additional_info(self) -> str:
        """Дополнительная информация о газонной траве"""
        return f"Страна: {self.country}, Цвет: {self.color}, " f"Срок прорастания: {self.germination_period} дней"

    def __str__(self) -> str:
        """Строковое представление газонной травы"""
        base_info = super().__str__()
        return f"{base_info}\n{self.additional_info}"

    @classmethod
    def create_product(cls, data: Dict[str, Any]) -> "LawnGrass":
        """Создание газонной травы из словаря"""
        return cls(
            name=str(data["name"]),
            description=str(data["description"]),
            price=float(data["price"]),
            quantity=int(data["quantity"]),
            country=str(data.get("country", "")),
            germination_period=int(data.get("germination_period", 0)),
            color=str(data.get("color", "")),
        )
