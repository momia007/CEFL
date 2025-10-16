# define el Blueprint
from flask import Blueprint

modulo_login_bp = Blueprint('modulo_login', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/modulo_login/static'
)