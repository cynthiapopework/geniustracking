import unittest
from unittest.mock import patch, Mock
from dhl.tracking.repository import get_tracking_info

class TestGetTrackingInfo(unittest.TestCase):

    @patch('dhl.tracking.repository.requests.get')
    def test_get_tracking_info(self, mock_get):
        # Mock response data
        mock_response_data = {
            "shipments": [
                {
                    "status": {
                        "status": "Shipment delivered"
                    },
                    "events": [
                        {
                            "timestamp": "2023-07-15T12:00:00Z",
                            "location": {
                                "address": {
                                    "addressLocality": "San Francisco"
                                }
                            },
                            "status": "Shipment delivered"
                        },
                        {
                            "timestamp": "2023-07-14T08:00:00Z",
                            "location": {
                                "address": {
                                    "addressLocality": "New York"
                                }
                            },
                            "status": "Shipment in transit"
                        }
                    ]
                }
            ]
        }
        
        # Configure the mock to return a response with the mocked data
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_response_data
        mock_get.return_value = mock_response
        
        # Call the function
        tracking_number = "7777777770"
        result = get_tracking_info(tracking_number)
        
        # Assert the result
        expected_result = {
            "shipments": [
                {
                    "status": "Shipment delivered",
                    "events": [
                        {
                            "timestamp": "2023-07-15T12:00:00Z",
                            "addressLocality": "San Francisco",
                            "status": "Shipment delivered"
                        },
                        {
                            "timestamp": "2023-07-14T08:00:00Z",
                            "addressLocality": "New York",
                            "status": "Shipment in transit"
                        }
                    ]
                }
            ]
        }
        self.assertEqual(result, expected_result)

    @patch('dhl.tracking.repository.requests.get')
    def test_get_tracking_info_no_shipments(self, mock_get):
        # Mock response data with no shipments
        mock_response_data = {
            "shipments": []
        }
        
        # Configure the mock to return a response with the mocked data
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_response_data
        mock_get.return_value = mock_response
        
        # Call the function
        tracking_number = "7777777770"
        result = get_tracking_info(tracking_number)
        
        # Assert the result
        expected_result = {
            "shipments": []
        }
        self.assertEqual(result, expected_result)

    @patch('dhl.tracking.repository.requests.get')
    def test_get_tracking_info_error(self, mock_get):
        # Configure the mock to return a response with a 404 status code
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.json.return_value = {
            "title": "No result found",
            "status": 404,
            "detail": "No shipment with given tracking number found."
        }
        mock_get.return_value = mock_response
        
        # Call the function and assert that it raises an error
        tracking_number = "7777777770"
        with self.assertRaises(Exception):
            get_tracking_info(tracking_number)

if __name__ == '__main__':
    unittest.main()
