import requests

# Define the base URL for the API
BASE_URL = "http://localhost:5000/api"

def call_tracking_endpoint(tracking_number):
    url = f"{BASE_URL}/tracking/{tracking_number}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Tracking Info:")
        print(response.json())
    else:
        print(f"Error: {response.status_code}")
        print(response.json())

def call_service_points_endpoint(country_code, address_locality, radius):
    url = f"{BASE_URL}/service_points"
    params = {
        "countryCode": country_code,
        "addressLocality": address_locality,
        "radius": radius
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print("Service Points Info:")
        print(response.json())
    else:
        print(f"Error: {response.status_code}")
        print(response.json())

if __name__ == "__main__":
    call_tracking_endpoint("7777777770")

    call_service_points_endpoint("US", "New York", 500)
