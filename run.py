from app import create_app
from flask_jwt_extended import JWTManager
from app.db_config import create_tables, create_admin,  destroy_tables

app = create_app()
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'

jwt = JWTManager(app)

@app.cli.command()
def migrate():
	create_tables()


@app.cli.command()
def drop():
	destroy_tables()

@app.cli.command()
def createAdmin():
	create_admin()