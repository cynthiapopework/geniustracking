from flask import Flask

from internal_api.routes import configure_routes

def create_app():
    app = Flask(__name__)
    configure_routes(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
