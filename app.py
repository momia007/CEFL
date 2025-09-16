from flask import Flask
from rutas.menu import menu_bp
from servicios.utils import obtener_version

app= Flask(__name__)

@app.context_processor
def inject_version():
    return dict(version=obtener_version())

app.register_blueprint(menu_bp)

if __name__ == '__main__':
    app.run(debug=True)