# Usuarios, roles, permisos
from servicios.db import db
from werkzeug.security import check_password_hash


class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id_usuario = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password_hash = db.Column(db.String(255))
    email = db.Column(db.String(100))
    fecha_creacion = db.Column(db.DateTime)
    activo = db.Column(db.Boolean)

    def verificar_password(self, password):
        return check_password_hash(self.password_hash, password)
