from src.types.http.http_request import HttpRequest
from src.types.http.http_response import HttpResponse
from .product_finder import ProductFinderView

class ProductsControllerMock:
    def __init__(self) -> None:
        self.find_by_name_attributes = {}

    def find_by_name(self, name: str) -> dict:
        self.find_by_name_attributes["name"] = name

def test_product_finder_view():
    products_controller = ProductsControllerMock()
    view = ProductFinderView(products_controller=products_controller)

    product_name = "Product 1"
    http_request = HttpRequest(body={ "name": product_name })

    response = view.handle(http_request)

    assert products_controller.find_by_name_attributes["name"] == product_name
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
