# Base URLs
DHL_BASE_URL = "https://api-eu.dhl.com"
DHL_SERVICE_POINT_BASE_URL = "https://api.dhl.com"

# Endpoints
TRACKING_ENDPOINT = "/track/shipments"
SERVICE_POINT_ENDPOINT = "/location-finder/v1/find-by-address"

DHL_TRACKING_URL = f"{DHL_BASE_URL}{TRACKING_ENDPOINT}"
DHL_SERVICE_POINT_URL = f"{DHL_SERVICE_POINT_BASE_URL}{SERVICE_POINT_ENDPOINT}"