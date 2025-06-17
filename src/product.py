from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __post_init__(self) -> None:
        if self.price <= 0:
            raise ValueError("Price must be positive")
        if self.quantity < 0:
            raise ValueError("Quantity can't be negative")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Product":
        """Создает продукт из словаря"""
        return cls(name=data["name"], description=data["description"], price=data["price"], quantity=data["quantity"])

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. (Осталось: {self.quantity})"
