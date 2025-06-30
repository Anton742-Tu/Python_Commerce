from src.product import Product


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self) -> str:
        base_info = super().__str__()
        return (
            f"{base_info}\n"
            f"Страна: {self.country}, Цвет: {self.color}\n"
            f"Срок прорастания: {self.germination_period} дней"
        )
