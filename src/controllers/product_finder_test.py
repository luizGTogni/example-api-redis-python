from pytest import raises
from src.types.errors.http_not_found import HttpNotFoundError
from .product_finder import ProductFinderController

class SqliteRepositoryMock:
    def __init__(self) -> None:
        self.find_product_by_name_attributes = {}

    def find_product_by_name(self, product_name: str) -> tuple:
        self.find_product_by_name_attributes["name"] = product_name
        return (0, product_name, 100.0, 10)

class SqliteRepositoryNotFoundMock:
    def find_product_by_name(self, product_name: str) -> tuple:
        raise HttpNotFoundError("Product not found")

class RedisRepositoryMock:
    def __init__(self) -> None:
        self.insert_attributes = {}
        self.get_key_attributes = {}

    def insert(self, key: str, value: str, expire_seconds: int = -1) -> None:
        self.insert_attributes["key"] = key
        self.insert_attributes["value"] = value
        self.insert_attributes["expire_seconds"] = expire_seconds

    def get_key(self, key: str) -> str:
        self.get_key_attributes["key"] = key

def test_find_product_by_name():
    sqlite_repository = SqliteRepositoryMock()
    redis_repository = RedisRepositoryMock()

    controller = ProductFinderController(
        sqlite_repository=sqlite_repository,
        redis_repository=redis_repository
    )

    product_name = "Product 1"
    controller.find_by_name(product_name)

    assert sqlite_repository.find_product_by_name_attributes["name"] == product_name
    assert redis_repository.insert_attributes["key"] == product_name
    assert redis_repository.insert_attributes["value"] == "100.0,10"
    assert redis_repository.insert_attributes["expire_seconds"] == 60
    assert redis_repository.get_key_attributes["key"] == product_name

def test_find_product_by_name_not_found():
    sqlite_repository = SqliteRepositoryNotFoundMock()
    redis_repository = RedisRepositoryMock()

    controller = ProductFinderController(
        sqlite_repository=sqlite_repository,
        redis_repository=redis_repository
    )

    with raises(HttpNotFoundError):
        controller.find_by_name(name="Product 1")
