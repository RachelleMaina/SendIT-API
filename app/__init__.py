from flask import Flask, Blueprint
from .api.v1 import version1_blueprint


def create_app():
	""""Method to initialize app."""
	app = Flask(__name__)

	app.register_blueprint(version1_blueprint, url_prefix = "/api/v1")

	return app
