from src.types.errors.http_error import HttpError
from src.types.http.http_response import HttpResponse

def handle_error(error: Exception) -> HttpResponse:
    if isinstance(error, HttpError):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
            status_code=500,
            body={
                "errors": [{
                    "title": "Server error",
                    "detail": str(error)
                }]
            }
        )
