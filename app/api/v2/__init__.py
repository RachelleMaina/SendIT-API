from flask import Blueprint
from flask_restful import Api, Resource
from .views.users_view import Register, Login


version2_blueprint = Blueprint('apiv2', __name__)
api = Api(version2_blueprint)
api.add_resource(Register, '/auth/signup')
api.add_resource(Login, '/auth/login')



