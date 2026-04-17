# modulo_login/rutas.py

# login, logout, perfil
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from backend.servicios.db import db
from functools import wraps
from backend.modulo_login.models import Usuario

modulo_login_bp = Blueprint('modulo_login', __name__, template_folder='templates')

@modulo_login_bp.route('/login', methods=['GET', 'POST'])
def login():
    print("Método:", request.method)
    if request.method == 'POST':
        print("POST recibido")
        print("DNI:", request.form.get('dni'))
        print("Password:", request.form.get('password'))

        usuario = Usuario.query.filter_by(dni=request.form['dni']).first()
        print("Usuario encontrado:", usuario)

        if usuario and usuario.check_password(request.form['password']):
            session['usuario'] = {
                'id': usuario.id_usuario,
                'nombre': f"{usuario.nombre} {usuario.apellido}",
                'nivel': usuario.nivel
            }
            print("Contraseña válida")
            flash('Login exitoso')
            return redirect(url_for('menu.inicio_usuarios'))
        else:
            print("Credenciales inválidas")
            flash('Credenciales inválidas')      
    return render_template('login.html')


def requiere_super(func):
    @wraps(func)   # <-- esta línea es la diferencia
    def wrapper(*args, **kwargs):
        if 'usuario' not in session or session['usuario']['nivel'] != 'Super':
            flash("Acceso restringido: solo Super puede crear usuarios")
            return redirect(url_for('login.login'))
        return func(*args, **kwargs)
    return wrapper

@modulo_login_bp.route('/usuarios/nuevo', methods=['GET','POST'])
@requiere_super
def nuevo_usuario():
    if request.method == 'POST':
        dni = request.form['dni']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        password = request.form['password']
        nivel = request.form['nivel']

        # Crear usuario
        nuevo = Usuario(
            dni=dni,
            nombre=nombre,
            apellido=apellido,
            email=email,
            nivel=nivel
        )
        nuevo.set_password(password)
        db.session.add(nuevo)
        db.session.commit()

        flash("Usuario creado correctamente")
        return redirect(url_for('menu.inicio'))

    return render_template('nuevo_usuario.html')
