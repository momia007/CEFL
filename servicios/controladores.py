# servicios/controladores.py

# lógica de autenticación y autorización

from flask import session, redirect, url_for, flash
from functools import wraps

def requiere_nivel(*niveles_permitidos):
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            usuario = session.get('usuario')
            print("Decorador: usuario en sesión:", usuario)
            if not usuario:
                flash('⚠️ No hay sesión activa')
                return redirect(url_for('modulo_login.login'))

            nivel = usuario.get('nivel')
            print("Decorador: nivel detectado:", nivel)
            if nivel not in niveles_permitidos:
                flash(f'⛔ Acceso denegado para nivel: {nivel}')
                return redirect(url_for('menu.inicio_usuarios'))
            return func(*args, **kwargs)
        return wrapper
    return decorador
