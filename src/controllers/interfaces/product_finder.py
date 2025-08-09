from abc import ABC, abstractmethod

class IProductFinderController(ABC):

    @abstractmethod
    def find_by_name(self, name: str) -> dict:
        pass
