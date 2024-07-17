from tracking.api import get_tracking_info
from service_point.api import get_service_points
from dotenv import load_dotenv

def main():
    load_dotenv()
    
    tracking_number = "7777777770"
    try:
        tracking_info = get_tracking_info(tracking_number)
        print("Tracking Information:")
        print(f"Shipment ID: {tracking_info.id}")
        print(f"Current Status: {tracking_info.status}")
        for event in tracking_info.tracking_events:
            print(f"{event.timestamp} - {event.location} - {event.status}")
    except Exception as e:
        print(f"Error fetching tracking information: {e}")
    
    country_code = "US"
    address_locality = "New York"
    radius = 500
    try:
        service_points = get_service_points(country_code, address_locality, radius)
        print("\nService Points:")
        for point in service_points.service_points:
            print(f"{point.name}, {point.address}")
    except Exception as e:
        print(f"Error fetching service points: {e}")

if __name__ == "__main__":
    main()
