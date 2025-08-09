from src.controllers.interfaces.product_finder import IProductFinderController
from src.types.http.http_request import HttpRequest
from src.types.http.http_response import HttpResponse
from .interfaces.view import IView

class ProductFinderView(IView):
    def __init__(self, products_controller: IProductFinderController) -> None:
        self.__products_controller = products_controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        name = http_request.params.get("name")
        body_response = self.__products_controller.find_by_name(name)
        return HttpResponse(status_code=200, body=body_response)
