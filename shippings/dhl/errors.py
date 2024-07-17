from .models import ErrorResponse

class DHLAPIError(Exception):
    """Base class for exceptions in this module."""
    pass

class AuthenticationError(DHLAPIError):
    """Raised when authentication fails."""
    pass

class NotFoundError(DHLAPIError):
    """Raised when the requested resource is not found."""
    def __init__(self, error_response: ErrorResponse):
        self.error_response = error_response
        super().__init__(self.error_response.detail)

class BadRequestError(DHLAPIError):
    """Raised when a bad request is made to the API."""
    def __init__(self, error_response: ErrorResponse):
        self.error_response = error_response
        super().__init__(self.error_response.detail)

class ServerError(DHLAPIError):
    """Raised when the server encounters an error."""
    def __init__(self, error_response: ErrorResponse):
        self.error_response = error_response
        super().__init__(self.error_response.detail)

def handle_response(response):
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:
        raise AuthenticationError("Authentication failed. Check your API key.")
    elif response.status_code == 404:
        error_data = response.json()
        error_response = ErrorResponse.from_api_response(error_data)
        raise NotFoundError(error_response)
    elif response.status_code == 400:
        error_data = response.json()
        error_response = ErrorResponse.from_api_response(error_data)
        raise BadRequestError(error_response)
    elif response.status_code >= 500:
        error_data = response.json()
        error_response = ErrorResponse.from_api_response(error_data)
        raise ServerError(error_response)
    e
