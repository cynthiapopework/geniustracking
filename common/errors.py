class DHLAPIError(Exception):
    """Base class for exceptions in this module."""
    pass

class AuthenticationError(DHLAPIError):
    """Raised when authentication fails."""
    pass

class NotFoundError(DHLAPIError):
    """Raised when the requested resource is not found."""
    def __init__(self, title: str, status: int, detail: str):
        self.title = title
        self.status = status
        self.detail = detail
        super().__init__(self.detail)

class BadRequestError(DHLAPIError):
    """Raised when a bad request is made to the API."""
    def __init__(self, title: str, status: int, detail: str):
        self.title = title
        self.status = status
        self.detail = detail
        super().__init__(self.detail)

class ServerError(DHLAPIError):
    """Raised when the server encounters an error."""
    def __init__(self, title: str, status: int, detail: str):
        self.title = title
        self.status = status
        self.detail = detail
        super().__init__(self.detail)

def handle_response(response):
    if response.status_code == 401:
        raise AuthenticationError("Authentication failed. Check your API key.")
    elif response.status_code == 404:
        error_data = response.json()
        raise NotFoundError(error_data.get('title', 'No title'), error_data.get('status', 404), error_data.get('detail', 'No detail'))
    elif response.status_code == 400:
        error_data = response.json()
        raise BadRequestError(error_data.get('title', 'No title'), error_data.get('status', 400), error_data.get('detail', 'No detail'))
    elif response.status_code >= 500:
        error_data = response.json()
        raise ServerError(error_data.get('title', 'No title'), error_data.get('status', 500), error_data.get('detail', 'No detail'))
    else:
        raise DHLAPIError(f"Unexpected error") 

