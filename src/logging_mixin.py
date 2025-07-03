import logging
from typing import Any, Tuple, Dict


class LoggingMixin:
    """Mixin class for logging object creation"""

    _init_args: Tuple[Any, ...]
    _init_kwargs: Dict[str, Any]
    _logger: logging.Logger

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize object with logging

        Args:
            *args: Positional arguments
            **kwargs: Keyword arguments
        """
        super().__init__(*args, **kwargs)  # type: ignore[call-arg]
        self._setup_logging()
        self._log_creation()

    def _setup_logging(self) -> None:
        """Configure logging settings"""
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        self._logger = logging.getLogger(self.__class__.__name__)

    def _log_creation(self) -> None:
        """Log object creation with parameters"""
        args_repr = [repr(arg) for arg in getattr(self, "_init_args", ())]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in getattr(self, "_init_kwargs", {}).items()]
        self._logger.info(f"Created {self.__class__.__name__} with args: {', '.join(args_repr + kwargs_repr)}")

    def __new__(cls, *args: Any, **kwargs: Any) -> Any:
        """Create new instance and store init arguments"""
        instance = super().__new__(cls)
        instance._init_args = args
        instance._init_kwargs = kwargs
        return instance
