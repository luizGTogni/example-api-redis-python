from pytest import raises
from src.types.http.http_request import HttpRequest
from src.types.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from .product_creator_validator import product_creator_validator

def test_creator_finder_validator_test():
    http_request = HttpRequest(body={
        "name": "Product 1",
        "price": 100,
        "quantity": 10
    })

    product_creator_validator(http_request)

def test_creator_finder_validator_test_error():
    http_request = HttpRequest(body={
        "price": 100,
        "quantity": 10
    })

    with raises(HttpUnprocessableEntityError):
        product_creator_validator(http_request)
