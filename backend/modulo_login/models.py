# cefl\backend\modulo_login\models.py

# Modelo de usuario para el módulo de login, con campos para DNI, nombre,
# apellido, contraseña, email, fecha de creación, estado activo y nivel de usuario.

from backend.servicios.db import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100))
    fecha_creacion = db.Column(db.DateTime, server_default=db.func.now())
    activo = db.Column(db.Boolean, default=True)
    nivel = db.Column(db.Enum(
        'Super','Admin','Dep-AlumnosFP','Alumno','Docente','Dep-Bachiller',
        name='nivel_enum'
    ), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
