from dhl.service_point.repository import get_service_points
from dhl.tracking.repository import get_tracking_info
from dotenv import load_dotenv

def main():
    load_dotenv()
    
    tracking_number = "7777777770"
    try:
        tracking_info = get_tracking_info(tracking_number)
        print(tracking_info)
    except Exception as e:
        print(f"Error fetching tracking information: {e}")
    
    country_code = "US"
    address_locality = "New York"
    radius = 500
    try:
        service_points = get_service_points(country_code, address_locality, radius)
        print(service_points)
    except Exception as e:
        print(f"Error fetching service points: {e}")

if __name__ == "__main__":
    main()
