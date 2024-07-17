import requests
from common.config import DHL_API_KEY
from common.errors import handle_response
from common.constants import DHL_TRACKING_URL
from .models import TrackingResponse

def get_tracking_info(tracking_number: str):
    url = f"{DHL_TRACKING_URL}?trackingNumber={tracking_number}"
    headers = {"DHL-API-Key": DHL_API_KEY}
    response = requests.get(url, headers=headers)
    print(response.text)
    data = handle_response(response)
    return TrackingResponse.from_api_response(data)

