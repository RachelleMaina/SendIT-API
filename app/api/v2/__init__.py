from flask import Blueprint
from flask_restful import Api, Resource

version2_blueprint = Blueprint('apiv2', __name__)
api = Api(version2_blueprint)


