from abc import ABC, abstractmethod
from typing import Dict


class BaseProduct(ABC):
    """Abstract base class defining the interface for all product types."""

    def __init__(self, name: str, description: str, price: float, quantity: int, **kwargs):
        """
        Initialize product with basic attributes.

        Args:
            name: Product name
            description: Product description
            price: Product price (must be positive)
            quantity: Product quantity in stock (must be non-negative)
            kwargs: Additional product-specific attributes
        """
        if price <= 0:
            raise ValueError("Price must be positive")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.description = description
        self._price = price  # Using protected attribute for price
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        """Return string representation of the product."""
        pass

    @property
    @abstractmethod
    def additional_info(self) -> str:
        """Return product-specific additional information."""
        pass

    @classmethod
    @abstractmethod
    def create_product(cls, data: Dict) -> "BaseProduct":
        """Create product instance from dictionary data."""
        pass

    @property
    def price(self) -> float:
        """Get the product price."""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """Set the product price with validation."""
        if value <= 0:
            raise ValueError("Price must be positive")
        self._price = value

    def apply_discount(self, discount: float) -> None:
        """
        Apply percentage discount to the product price.

        Args:
            discount: Discount percentage (0 < discount <= 1)

        Raises:
            ValueError: If discount is not in valid range
        """
        if not 0 < discount <= 1:
            raise ValueError("Discount must be between 0 and 1")
        self._price *= 1 - discount
