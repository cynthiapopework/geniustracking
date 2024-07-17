from typing import Optional
import requests

from common.config import DHL_API_KEY
from common.errors import handle_response
from .models import ServicePointsResponse

def get_service_points(country_code: str, address_locality: str, radius: Optional[int] = None):
    if radius:
        radius_param = radius 
    else: 
        radius = 0 
    url = f"https://api.dhl.com/location-finder/v1/find-by-address?countryCode={country_code}&addressLocality={address_locality}&radius={radius_param}"
    headers = {"DHL-API-Key": DHL_API_KEY}
    response = requests.get(url, headers=headers)
    print(response.text)
    data = handle_response(response)
    return ServicePointsResponse.from_api_response(data)
