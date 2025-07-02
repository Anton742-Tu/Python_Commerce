from src.product import Product


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: int, color: str):
        """
        Трава газонная - наследник Product
        :param country: Страна-производитель
        :param germination_period: Срок прорастания (дни)
        :param color: Цвет
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    @property
    def additional_info(self) -> str:
        """Дополнительная информация о траве"""
        return (f"Страна: {self.country}, Цвет: {self.color}, "
                f"Срок прорастания: {self.germination_period} дней")

    def __str__(self) -> str:
        """Строковое представление травы"""
        base_info = super().__str__()
        return f"{base_info}\n{self.additional_info}"
