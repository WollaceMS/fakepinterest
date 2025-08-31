from fakepinterest import app, database
from fakepinterest.models import Foto, Usuario


with app.app_context():
    database.create_all()