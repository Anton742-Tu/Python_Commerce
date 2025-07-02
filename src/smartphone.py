from src.product import Product


class Smartphone(Product):
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
        **kwargs,
    ):
        """
        Smartphone product class inheriting from Product.

        Args:
            name: Product name
            description: Product description
            price: Product price (must be positive)
            quantity: Initial stock quantity
            performance: CPU performance in GHz (must be positive)
            model: Device model name
            memory: RAM capacity in GB (must be positive)
            color: Device color
            kwargs: Additional product attributes
        """
        super().__init__(name, description, price, quantity, **kwargs)

        if performance <= 0:
            raise ValueError("Performance must be positive")
        if memory <= 0:
            raise ValueError("Memory must be positive")

        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    @property
    def additional_info(self) -> str:
        """Returns detailed smartphone specifications."""
        return (
            f"Model: {self.model}, Color: {self.color}, "
            f"Performance: {self.performance}GHz, Memory: {self.memory}GB"
        )

    def __str__(self) -> str:
        """String representation combining base product info and smartphone details."""
        return f"{super().__str__()}\n{self.additional_info}"

    @classmethod
    def create_product(cls, data: dict) -> "Smartphone":
        """Factory method to create smartphone from dictionary data."""
        return cls(
            name=str(data["name"]),
            description=str(data["description"]),
            price=float(data["price"]),
            quantity=int(data["quantity"]),
            performance=float(data.get("performance", 0)),
            model=str(data.get("model", "Unknown")),
            memory=int(data.get("memory", 0)),
            color=str(data.get("color", "Unknown")),
        )
