import requests
from common.config import DHL_API_KEY
from common.errors import handle_response
from common.constants import DHL_TRACKING_URL

def get_tracking_info(tracking_number: str):
    url = f"{DHL_TRACKING_URL}?trackingNumber={tracking_number}"
    headers = {"DHL-API-Key": DHL_API_KEY}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if not data['shipments']:
            return {"shipments": []}
        
        shipments_info = []
        for shipment in data['shipments']:
            status = shipment.get('status', {}).get('status', 'No status')
            events = [
                {
                    "timestamp": event.get("timestamp"),
                    "addressLocality": event.get("location", {}).get("address", {}).get("addressLocality", "Unknown location"),
                    "status": event.get("status", "No status")
                } for event in shipment.get('events', [])
            ]
            shipments_info.append({"status": status, "events": events})
        
        return {"shipments": shipments_info}
    else:
        handle_response(response)