import logging
from typing import Any


class LoggingMixin:
    """Mixin class for logging object creation and initialization.

    Provides automatic logging when objects are created, including:
    - Class name
    - Positional arguments
    - Keyword arguments
    """

    def __init__(self, *args, **kwargs):
        """Initialize the object and log creation parameters.

        Args:
            *args: Positional arguments passed to constructor
            **kwargs: Keyword arguments passed to constructor
        """
        super().__init__(*args, **kwargs)
        self._setup_logging()

    def _setup_logging(self) -> None:
        """Configure logging settings for the mixin."""
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        self._logger = logging.getLogger(self.__class__.__name__)

    def _log_creation(self) -> None:
        """Log object creation with initialization parameters."""
        class_name = self.__class__.__name__

        # Format arguments for logging
        args_repr = [repr(arg) for arg in self._init_args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in self._init_kwargs.items()]
        all_args = ", ".join(args_repr + kwargs_repr)

        self._logger.info(f"Created {class_name} instance with args: {all_args}")

    def __new__(cls, *args: Any, **kwargs: Any) -> Any:
        """Override __new__ to capture initialization parameters."""
        instance = super().__new__(cls)
        instance._init_args = args
        instance._init_kwargs = kwargs
        return instance

    def __init_subclass__(cls, **kwargs: Any) -> None:
        """Ensure proper initialization in subclasses."""
        super().__init_subclass__(**kwargs)
        cls._logger = logging.getLogger(cls.__name__)
