from flask import Blueprint, render_template, request, redirect, url_for
from servicios.slider import obtener_slider
from servicios.utils import ordenar_paises
from servicios.paises import obtener_paises
from servicios.provincias import obtener_provincias
from servicios.cursos import insertar_curso
from servicios.cursos import obtener_cursos
from collections import defaultdict
from servicios.utils import formatear_hora


menu_bp = Blueprint('menu', __name__)

@menu_bp.route('/')
def inicio():
    slider = obtener_slider('slider_inicio')  # Ajusta el nombre de la carpeta según sea necesario
    return render_template('inicio.html', slider=slider)

@menu_bp.route('/inscripciones')
def inscripciones():

    paises_raw = obtener_paises()
    paises = ordenar_paises(paises_raw)

    provincias = obtener_provincias()

    cursos_raw = obtener_cursos()

    cursos_por_nik = defaultdict(list)
    for curso in cursos_raw:
        print(curso['dias'], type(curso['dias']))
        hora_inicio = formatear_hora(curso['hora_inicio'])
        hora_fin = formatear_hora(curso['hora_fin'])
        dias = curso['dias']

        cursos_por_nik[curso['nikname']].append({
            'id': curso['id_curso'],
            'horario': f"{hora_inicio} a {hora_fin} hs",
            'modalidad': curso['modalidad'],
            'dias': dias
        })
    print("Provincias:", provincias)
    return render_template('inscripciones.html', paises=paises, provincias=provincias, cursos_por_nik=cursos_por_nik)

@menu_bp.route('/eventos')
def eventos():
    slider_e = obtener_slider('slider_eventos')  # Ajusta el nombre de la carpeta según sea necesario
    return render_template('eventos.html', slider=slider_e)

@menu_bp.route('/admin/cursos', methods=['GET', 'POST'])
def admin_cursos():
    # ⚠️ Vista privada: en el futuro, agregar verificación de login y permisos
    # Ejemplo:
    # if not usuario_logueado or not usuario.tiene_permiso('admin_cursos'):
    #     return redirect(url_for('login'))

    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.form.get('nombre')
        nikname = request.form.get('nikname')
        descripcion = request.form.get('descripcion') or None
        cuatrimestre = int(request.form.get('cuatrimestre'))
        anio = request.form.get('anio') or None
        modalidad = request.form.get('modalidad')
        activo = int(request.form.get('activo', 1))  # Checkbox activo
        hora_inicio = request.form.get('hora_inicio') or None
        hora_fin = request.form.get('hora_fin') or None
        dias = request.form.getlist('dias')  # Captura todos los días seleccionados
        dias_str = ','.join(dias) if dias else None  # Convierte a texto para guardar


        # Insertar curso en la base
        insertar_curso(nombre, nikname, descripcion, cuatrimestre, anio, modalidad, activo, hora_inicio, hora_fin, dias_str)

        # Redirigir a la misma vista (limpiar formulario)
        return redirect(url_for('menu.admin_cursos'))

    # Renderizar formulario vacío
    return render_template('admin_cursos.html')

@menu_bp.route('/admin/listado_cursos')
def listado_cursos():
    cursos = obtener_cursos()
    return render_template('listado_cursos.html', cursos=cursos)

@menu_bp.route('/admin/inicio_usuarios')
def inicio_usuarios():
    return render_template('inicio_usuarios.html')


