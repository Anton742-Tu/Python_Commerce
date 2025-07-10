class ZeroQuantityError(ValueError):
    """Исключение для случая добавления товара с нулевым количеством"""

    def __init__(self, message: str = "Товар с нулевым количеством не может быть добавлен"):
        self.message = message
        super().__init__(message)
