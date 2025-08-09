from .http_error import HttpError

class HttpNotFoundError(HttpError):
    def __init__(self, message: str) -> None:
        super().__init__(status_code=404, name="NotFound", message=message)
