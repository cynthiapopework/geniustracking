from flask import Blueprint, request, jsonify
from dhl.tracking.repository import get_tracking_info
from dhl.service_point.repository import get_service_points

api_bp = Blueprint('api', __name__)

@api_bp.route('/tracking/<tracking_number>', methods=['GET'])
def tracking(tracking_number):
    try:
        tracking_info = get_tracking_info(tracking_number)
        if not tracking_info['shipments']:
            return jsonify({"message": "No tracking information found for this shipment."}), 404
        return jsonify(tracking_info), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_bp.route('/service_points', methods=['GET'])
def service_points():
    country_code = request.args.get('countryCode')
    address_locality = request.args.get('addressLocality')
    radius = request.args.get('radius', type=int, default=0)

    try:
        service_points_info = get_service_points(country_code, address_locality, radius)
        return jsonify(service_points_info), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def configure_routes(app):
    app.register_blueprint(api_bp, url_prefix='/api')
