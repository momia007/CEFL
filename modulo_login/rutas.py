# modulo_login/rutas.py

# login, logout, perfil
from flask import render_template, request, redirect, url_for, session, flash
from modulo_login.blueprint import modulo_login_bp
from modulo_login.modelos import Usuario


@modulo_login_bp.route('/login', methods=['GET', 'POST'])
def login():
    print("Método:", request.method)
    if request.method == 'POST':
        print("POST recibido")
        print("Email:", request.form.get('email'))
        print("Password:", request.form.get('password'))

        usuario = Usuario.query.filter_by(email=request.form['email']).first()
        print("Usuario encontrado:", usuario)

        if usuario and usuario.verificar_password(request.form['password']):
            session['usuario'] = {
                'id': usuario.id_usuario,
                'nombre': usuario.username,
                'nivel': usuario.nivel
}
            print("Contraseña válida")
            session['usuario_id'] = usuario.id_usuario
            flash('Login exitoso')
            return redirect(url_for('menu.inicio_usuarios'))
        else:
            print("Credenciales inválidas")
            flash('Credenciales inválidas')      
    return render_template('login.html')


#@modulo_login_bp.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method == 'POST':
#        usuario = Usuario.query.filter_by(email=request.form['email']).first()
#        if usuario and usuario.verificar_password(request.form['password']):
#            session['usuario_id'] = usuario.id_usuario
#            session['rol'] = usuario.rol
#            session['empresa_id'] = usuario.empresa_id

#            flash('Login exitoso')
#            return redirect(url_for('menu.inicio'))
#        else:
#            flash('Credenciales inválidas')
            
#    return render_template('login.html')
