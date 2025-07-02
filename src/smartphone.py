from src.product import Product


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 performance: float, model: str, memory: int, color: str):
        """
        Смартфон - наследник Product
        :param performance: Производительность (GHz)
        :param model: Модель
        :param memory: Объем памяти (GB)
        :param color: Цвет
        """
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    @property
    def additional_info(self) -> str:
        """Дополнительная информация о смартфоне"""
        return (f"Модель: {self.model}, Цвет: {self.color}, "
                f"Производительность: {self.performance} GHz, Память: {self.memory}GB")

    def __str__(self) -> str:
        """Строковое представление смартфона"""
        base_info = super().__str__()
        return f"{base_info}\n{self.additional_info}"
