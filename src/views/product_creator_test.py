from src.types.http.http_request import HttpRequest
from src.types.http.http_response import HttpResponse
from .product_creator import ProductCreatorView

class ProductsControllerMock:
    def __init__(self) -> None:
        self.create_attributes = {}

    def create(self, name: str, price: float, quantity: int) -> dict:
        self.create_attributes["name"] = name
        self.create_attributes["price"] = price
        self.create_attributes["quantity"] = quantity

def test_product_creator_view():
    products_controller = ProductsControllerMock()
    view = ProductCreatorView(products_controller=products_controller)

    product_name = "Product 1"
    price = 100
    quantity = 10
    http_request = HttpRequest(
        body={
            "name": product_name,
            "price": price,
            "quantity": quantity
        }
    )

    response = view.handle(http_request)

    assert products_controller.create_attributes["name"] == product_name
    assert products_controller.create_attributes["price"] == price
    assert products_controller.create_attributes["quantity"] == quantity
    assert isinstance(response, HttpResponse)
    assert response.status_code == 201
