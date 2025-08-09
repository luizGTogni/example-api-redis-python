from .http_error import HttpError

class HttpUnprocessableEntityError(HttpError):
    def __init__(self, message: str) -> None:
        super().__init__(status_code=422, name="UnprocessableEntity", message=message)
