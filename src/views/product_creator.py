from src.controllers.interfaces.product_creator import IProductCreatorController
from src.types.http.http_request import HttpRequest
from src.types.http.http_response import HttpResponse
from .validators.product_creator_validator import product_creator_validator
from .interfaces.view import IView

class ProductCreatorView(IView):
    def __init__(self, products_controller: IProductCreatorController) -> None:
        self.__products_controller = products_controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        product_creator_validator(http_request)
        name = http_request.body["name"]
        price = http_request.body["price"]
        quantity = http_request.body["quantity"]
        body_response = self.__products_controller.create(name, price, quantity)
        return HttpResponse(status_code=201, body=body_response)
