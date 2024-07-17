from typing import List, Dict
from common.models import BaseModel

class ServicePoint(BaseModel):
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    @classmethod
    def from_api_response(cls, data: Dict):
        return cls(
            name=data.get('name', 'No name'),
            address=data.get('address', 'No address')
        )

class ServicePointsResponse(BaseModel):
    def __init__(self, service_points: List[ServicePoint]):
        self.service_points = service_points

    @classmethod
    def from_api_response(cls, data: Dict):
        points = data.get('locations', [])
        service_points = [ServicePoint.from_api_response(point) for point in points]
        return cls(service_points=service_points)
