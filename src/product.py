from typing import Dict, Any


class Product:
    def init(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Product:
        """Создает продукт из словаря"""
        return cls(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            quantity=data['quantity']
        )

    def str(self):
        return f"{self.name}, {self.price} руб. (Осталось: {self.quantity})"
