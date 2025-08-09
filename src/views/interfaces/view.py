from abc import ABC, abstractmethod
from src.types.http.http_request import HttpRequest
from src.types.http.http_response import HttpResponse

class IView(ABC):

    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pass
