from flask import Flask
from rutas.menu import menu_bp
from servicios.utils import obtener_version
from servicios.db import db
from modulo_login import modulo_login_bp
from dotenv import load_dotenv
import os

load_dotenv() # Cargar variables de entorno

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Construir la url desde variables
usuario = os.getenv('DB_USER')
clave = os.getenv('DB_PASS')
host = os.getenv('DB_HOST')
base = os.getenv('DB_NAME')



# ✅ CONFIGURACIÓN DE BASE DE DATOS
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{usuario}:{clave}@{host}/{base}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ✅ INICIALIZAR SQLAlchemy
db.init_app(app)

@app.context_processor
def inject_version():
    return dict(version=obtener_version())

# ✅ REGISTRAR BLUEPRINTS
app.register_blueprint(menu_bp)
app.register_blueprint(modulo_login_bp, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)
