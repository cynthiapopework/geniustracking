from shippings.dhl.api import get_tracking_info, get_service_points
from dotenv import load_dotenv

def main():
    load_dotenv()
    
    tracking_number = "7777777770"
    try:
        tracking_info = get_tracking_info(tracking_number)
        print("Tracking Information:")
        for event in tracking_info.tracking_events:
            print(event.description)
    except Exception as e:
        print(f"Error fetching tracking information: {e}")
    
    country_code = "US"
    city = "New York"
    radius = 500
    try:
        service_points = get_service_points(country_code, city, radius)
        print("\nService Points:")
        for point in service_points.service_points:
            print(f"{point.name}, {point.address}")
    except Exception as e:
        print(f"Error fetching service points: {e}")

if __name__ == "__main__":
    main()
