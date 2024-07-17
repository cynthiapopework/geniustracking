from typing import Dict

class BaseModel:
    @classmethod
    def from_api_response(cls, data: Dict):
        raise NotImplementedError("Subclasses must implement from_api_response method")

class ErrorResponse(BaseModel):
    def __init__(self, title: str, status: int, detail: str):
        self.title = title
        self.status = status
        self.detail = detail

    @classmethod
    def from_api_response(cls, data: Dict):
        return cls(
            title=data.get('title', 'No title'),
            status=data.get('status', 0),
            detail=data.get('detail', 'No detail')
        )
