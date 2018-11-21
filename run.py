from app import create_app
from flask_jwt_extended import JWTManager

app = create_app()
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'

jwt = JWTManager(app)

