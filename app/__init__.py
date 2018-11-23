import os
from flask import Flask, Blueprint
from flask_mail import Mail
from instance.config import Config
from flask_jwt_extended import JWTManager
from flask import Flask, Blueprint, make_response, jsonify
from flask_mail import Mail
from .api.v1 import version1_blueprint
from .api.v2 import version2_blueprint


def init():
    """Method to initialize app"""
    app = Flask(__name__)
    return app


def send_email():
    """Method to add mail object to app"""
    app = init()
    app.config.update(dict(
        MAIL_SERVER='smtp.googlemail.com',
        MAIL_PORT=465,
        MAIL_USE_TLS=False,
        MAIL_USE_SSL=True,
        MAIL_USERNAME=os.environ.get('MAIL_USERNAME'),
        MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD'),
        SENDER=os.environ.get('SENDER')
    ))
    mail = Mail(app)
    return mail

def page_not_found(e):
    return make_response(jsonify(
        {
            "Message": "url given not available in this server"
        }), 404)


def handle_server_error(e):
    return make_response(jsonify(
        {
            "Message": "Internal Server Error"
        }), 500)

def create_app():
    app = init()
    send_email()
    jwt = JWTManager(app)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['JWT_SECRET_KEY'] = 'jwt-rakeli'
    app.register_blueprint(version1_blueprint, url_prefix="/api/v1")
    app.register_blueprint(version2_blueprint, url_prefix="/api/v2")
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, handle_server_error)
    return app
