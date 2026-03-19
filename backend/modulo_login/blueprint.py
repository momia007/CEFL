# backend/modulo_login/blueprint.py

from flask import Blueprint

modulo_login_bp = Blueprint(
    'login', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/login/static'
)
