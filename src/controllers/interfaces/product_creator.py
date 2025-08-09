from abc import ABC, abstractmethod

class IProductCreatorController(ABC):

    @abstractmethod
    def create(self, name: str, price: float, quantity: int) -> dict:
        pass
