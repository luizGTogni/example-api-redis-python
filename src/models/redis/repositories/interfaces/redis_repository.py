from abc import ABC, abstractmethod

class IRedisRepository(ABC):

    @abstractmethod
    def insert(self, key: str, value: str, expire_seconds: int = -1) -> None:
        pass

    @abstractmethod
    def get_key(self, key: str) -> str:
        pass

    @abstractmethod
    def insert_hash(self, key: str, field: str, value: str, expire_seconds: int = -1) -> None:
        pass

    @abstractmethod
    def get_hash(self, key: str, field: str) -> str:
        pass
