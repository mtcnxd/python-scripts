from abc import abstractmethod
from typing import Protocol

class AbstractCurrency (Protocol):
    @abstractmethod
    def set_price(self) -> str:
        pass

    @abstractmethod
    def set_book(self) -> str:
        pass