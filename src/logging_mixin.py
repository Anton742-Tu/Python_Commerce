class LoggingMixin:
    """Миксин для логирования создания объектов"""

    def __init__(self, *args, **kwargs):
        """Логирует параметры создания объекта"""
        super().__init__(*args, **kwargs)

        # Получаем имя класса
        class_name = self.__class__.__name__

        # Формируем строку с параметрами
        init_params = []
        if args:
            init_params.extend(repr(arg) for arg in args)
        if kwargs:
            init_params.extend(f"{key}={repr(value)}" for key, value in kwargs.items())

        params_str = ", ".join(init_params)

        # Выводим информацию в консоль
        print(f"Создан объект {class_name}({params_str})")
