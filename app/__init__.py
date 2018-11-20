from instance.config import Config
from werkzeug.exceptions import HTTPException
from flask import Flask, Blueprint, make_response, jsonify
from .api.v1 import version1_blueprint
from .api.v2 import version2_blueprint


def page_not_found(e):
    return make_response(jsonify(
        {
            "Message": "url given not available in this server"
        }), 404)

def handle_bad_request(e):
    return 'bad request!', 400

def create_app(config_class=Config):
    """"Method to initialize app."""
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.register_blueprint(version1_blueprint, url_prefix="/api/v1")
    app.register_blueprint(version2_blueprint, url_prefix="/api/v2")
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(400, handle_bad_request)

    return app


