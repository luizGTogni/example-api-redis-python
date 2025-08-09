from src.models.sqlite.repositories.interfaces.products_repository import IProductsRepository
from src.models.redis.repositories.interfaces.redis_repository import IRedisRepository
from src.types.errors.http_not_found import HttpNotFoundError
from .interfaces.product_finder import IProductFinderController

class ProductFinderController(IProductFinderController):
    def __init__(
            self,
            sqlite_repository: IProductsRepository,
            redis_repository: IRedisRepository
        ) -> None:
        self.__sqlite_repository = sqlite_repository
        self.__redis_repository = redis_repository

    def find_by_name(self, name: str) -> dict:
        product = self.__find_product(name)
        return self.__format_response(product)

    def __find_product(self, name) -> tuple:
        product = self.__find_in_cache(name)

        if not product:
            product = self.__find_in_sql(name)
            self.__insert_in_cache(product)

        return product

    def __find_in_cache(self, name: str) -> tuple:
        product_str = self.__redis_repository.get_key(name)

        if not product_str:
            return None

        price, quantity = product_str.split(",")
        return (0, name, price, quantity)

    def __find_in_sql(self, name: str) -> tuple:
        product = self.__sqlite_repository.find_product_by_name(name)

        if not product:
            raise HttpNotFoundError("Product not found")

        return product

    def __insert_in_cache(self, product: tuple) -> None:
        name = product[1]
        price = product[2]
        quantity = product[3]

        value = f"{price},{quantity}"
        self.__redis_repository.insert(key=name, value=value, expire_seconds=60)

    def __format_response(self, product: tuple) -> dict:
        name = product[1]
        price = product[2]
        quantity = product[3]

        return {
            "data": {
                "type": "Product",
                "count": 1,
                "attributes": {
                    "product_name": name,
                    "price": price,
                    "quantity": quantity
                }
            }
        }
