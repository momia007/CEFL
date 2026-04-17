# cefl\backend\app.py

from flask import Flask
from backend.rutas.menu import menu_bp
from backend.rutas.inscripciones import inscripciones_bp
from backend.servicios.utils import obtener_version
from backend.servicios.db import db, get_connection
from backend.modulo_login import modulo_login_bp
from dotenv import load_dotenv
import os


# ✅ Cargar variables de entorno
load_dotenv()

app = Flask(__name__, template_folder="templates", static_folder="../frontend/static")
app.secret_key = os.getenv('SECRET_KEY')

# ✅ Configuración de base de datos
usuario = os.getenv('DB_USER')
clave = os.getenv('DB_PASS')
host = os.getenv('DB_HOST')
base = os.getenv('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{usuario}:{clave}@{host}/{base}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ✅ Inicializar SQLAlchemy
db.init_app(app)

# ✅ Context processors
@app.context_processor
def inject_config():
    conn = get_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT valor FROM configuracion WHERE clave = 'inscripciones_habilitadas'")
            resultado = cursor.fetchone()
        conn.close()
        return {'inscripciones_habilitadas': resultado['valor'] if resultado else 'no'}
    return {'inscripciones_habilitadas': 'no'}

@app.context_processor
def inject_version():
    return dict(version=obtener_version())

# ✅ Registrar blueprints
app.register_blueprint(menu_bp)
app.register_blueprint(modulo_login_bp, url_prefix='/auth')
app.register_blueprint(inscripciones_bp)

if __name__ == '__main__':
    app.run(debug=True)
