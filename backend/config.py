# cefl\backend\config.py

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///cflb.db'  # o tu URI real
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'clave_segura'

# Variable de control de inscripciones
INSCRIPCIONES_HABILITADAS = False  # cambiar a True cuando se habiliten
