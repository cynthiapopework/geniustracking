from typing import List, Dict
from common.models import BaseModel

class TrackingEvent(BaseModel):
    def __init__(self, timestamp: str, location: str, status: str):
        self.timestamp = timestamp
        self.location = location
        self.status = status

    @classmethod
    def from_api_response(cls, data: Dict):
        location = data.get('location', {}).get('address', {}).get('addressLocality', 'Unknown location')
        return cls(
            timestamp=data.get('timestamp', 'No timestamp'),
            location=location,
            status=data.get('status', 'No status')
        )

class TrackingResponse(BaseModel):
    def __init__(self, tracking_events: List[TrackingEvent], id: str, status: str):
        self.tracking_events = tracking_events
        self.id = id
        self.status = status

    @classmethod
    def from_api_response(cls, data: Dict):
        shipment = data['shipments'][0]
        tracking_events = [TrackingEvent.from_api_response(event) for event in shipment.get('events', [])]
        return cls(
            tracking_events=tracking_events,
            id=shipment.get('id', 'No ID'),
            status=shipment.get('status', {}).get('status', 'No status')
        )
