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
        **kwargs,
    ):
        """
        Lawn grass product class inheriting from Product.

        Args:
            name: Product name
            description: Product description
            price: Product price (must be positive)
            quantity: Initial stock quantity
            country: Country of origin
            germination_period: Germination period in days (must be positive)
            color: Grass color
            kwargs: Additional product attributes
        """
        super().__init__(name, description, price, quantity, **kwargs)

        if germination_period <= 0:
            raise ValueError("Germination period must be positive")

        self.country = country
        self.germination_period = germination_period
        self.color = color

    @property
    def additional_info(self) -> str:
        """Returns detailed lawn grass specifications."""
        return f"Страна: {self.country}, Цвет: {self.color}, " f"Срок прорастания: {self.germination_period} дней"

    def __str__(self) -> str:
        """String representation combining base product info and lawn grass details."""
        return f"{super().__str__()}\n{self.additional_info}"

    @classmethod
    def create_product(cls, data: dict) -> "LawnGrass":
        """Factory method to create lawn grass product from dictionary data."""
        return cls(
            name=str(data["name"]),
            description=str(data["description"]),
            price=float(data["price"]),
            quantity=int(data["quantity"]),
            country=str(data.get("country", "Unknown")),
            germination_period=int(data.get("germination_period", 0)),
            color=str(data.get("color", "Unknown")),
        )
