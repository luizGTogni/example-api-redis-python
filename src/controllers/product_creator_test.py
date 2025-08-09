from .product_creator import ProductCreatorController

class SqliteRepositoryMock:
    def __init__(self) -> None:
        self.insert_product_attributes = {}

    def insert_product(self, name: str, price: float, quantity: int) -> None:
        self.insert_product_attributes["name"] = name
        self.insert_product_attributes["price"] = price
        self.insert_product_attributes["quantity"] = quantity

class RedisRepositoryMock:
    def __init__(self) -> None:
        self.insert_attributes = {}

    def insert(self, key: str, value: str, expire_seconds: int = -1) -> None:
        self.insert_attributes["key"] = key
        self.insert_attributes["value"] = value
        self.insert_attributes["expire_seconds"] = expire_seconds

def test_create_product():
    sqlite_repository = SqliteRepositoryMock()
    redis_repository = RedisRepositoryMock()

    controller = ProductCreatorController(
        sqlite_repository=sqlite_repository,
        redis_repository=redis_repository
    )

    product_name = "Product 1"
    price = 100.0
    quantity = 10
    response = controller.create(product_name, price, quantity)

    assert sqlite_repository.insert_product_attributes["name"] == product_name
    assert sqlite_repository.insert_product_attributes["price"] == price
    assert sqlite_repository.insert_product_attributes["quantity"] == quantity
    assert redis_repository.insert_attributes["key"] == product_name
    assert redis_repository.insert_attributes["value"] == "100.0,10"
    assert redis_repository.insert_attributes["expire_seconds"] == 60
    assert response == {
        "data": {
            "type": "Product",
            "count": 1,
            "message": "Product created sucessfully"
        }
    }
