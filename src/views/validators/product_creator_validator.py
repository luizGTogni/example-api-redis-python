from pydantic import BaseModel, ValidationError
from src.types.http.http_request import HttpRequest
from src.types.errors.http_unprocessable_entity import HttpUnprocessableEntityError

def product_creator_validator(http_request: HttpRequest) -> None:
    class BodyData(BaseModel):
        name: str
        price: float
        quantity: int

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
