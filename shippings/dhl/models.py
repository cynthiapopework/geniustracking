from typing import Dict, List


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

class TrackingEvent(BaseModel):
    def __init__(self, description: str):
        self.description = description

    @classmethod
    def from_api_response(cls, data: Dict):
        return cls(
            description=data.get('status', {}).get('description', 'No status description')
        )

class TrackingResponse(BaseModel):
    def __init__(self, tracking_events: List[TrackingEvent]):
        self.tracking_events = tracking_events

    @classmethod
    def from_api_response(cls, data: Dict):
        shipments = data.get('shipments', [])
        tracking_events = [TrackingEvent.from_api_response(shipment) for shipment in shipments]
        return cls(tracking_events=tracking_events)
    
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

class TrackingResponse(BaseModel):
    def __init__(self, tracking_events: List[TrackingEvent]):
        self.tracking_events = tracking_events

    @classmethod
    def from_api_response(cls, data: Dict):
        shipments = data.get('shipments', [])
        tracking_events = [TrackingEvent.from_api_response(shipment) for shipment in shipments]
        return cls(tracking_events=tracking_events)

class ServicePointsResponse(BaseModel):
    def __init__(self, service_points: List[ServicePoint]):
        self.service_points = service_points

    @classmethod
    def from_api_response(cls, data: Dict):
        points = data.get('servicePoints', [])
        service_points = [ServicePoint.from_api_response(point) for point in points]
        return cls(service_points=service_points)
