import requests
from common.config import DHL_API_KEY
from common.errors import handle_response
from common.constants import DHL_SERVICE_POINT_URL
from .models import ServicePointsResponse
from typing import Optional

def get_service_points(country_code: str, address_locality: str, radius: Optional[int] = None):
    radius_param = radius if radius is not None else 0
    url = f"{DHL_SERVICE_POINT_URL}?countryCode={country_code}&addressLocality={address_locality}&radius={radius_param}"
    headers = {"DHL-API-Key": DHL_API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        service_points_info = []
        for location in data.get('locations', []):
            service_point = {
                'distance': location.get('distance'),
                'address': location.get('place', {}).get('address', {})
            }
            service_points_info.append(service_point)
        return {'service_points': service_points_info}
    else:
        handle_response(response)