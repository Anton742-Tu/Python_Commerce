from src.product import Product


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self) -> str:
        base_info = super().__str__()
        return (
            f"{base_info}\n"
            f"Модель: {self.model}, Цвет: {self.color}\n"
            f"Производительность: {self.efficiency} GHz, Память: {self.memory}GB"
        )
