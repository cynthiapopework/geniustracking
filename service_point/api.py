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
    print(response.text)
    data = handle_response(response)
    return ServicePointsResponse.from_api_response(data)