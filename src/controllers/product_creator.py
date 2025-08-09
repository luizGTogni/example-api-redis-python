from src.models.sqlite.repositories.interfaces.products_repository import IProductsRepository
from src.models.redis.repositories.interfaces.redis_repository import IRedisRepository
from .interfaces.product_creator import IProductCreatorController

class ProductCreatorController(IProductCreatorController):
    def __init__(
            self,
            sqlite_repository: IProductsRepository,
            redis_repository: IRedisRepository
        ) -> None:
        self.__sqlite_repository = sqlite_repository
        self.__redis_repository = redis_repository

    def create(self, name: str, price: float, quantity: int) -> dict:
        self.__insert_in_sql(name, price, quantity)
        self.__insert_in_cache(name, price, quantity)
        return self.__format_response()

    def __insert_in_sql(self, name: str, price: float, quantity: int) -> None:
        self.__sqlite_repository.insert_product(name, price, quantity)

    def __insert_in_cache(self, name: str, price: float, quantity: int) -> None:
        value = f"{price},{quantity}"
        self.__redis_repository.insert(key=name, value=value, expire_seconds=60)

    def __format_response(self) -> dict:
        return {
            "data": {
                "type": "Product",
                "count": 1,
                "message": "Product created sucessfully"
            }
        }
