# archivo: rutas/inscripciones.py

from flask import Blueprint, request, redirect, url_for, flash, render_template, session
from backend.servicios.db import get_connection
from backend.servicios.paises import obtener_paises
from backend.servicios.provincias import obtener_provincias
from backend.servicios.cursos import obtener_cursos
from backend.servicios.utils import ordenar_paises, formatear_hora
from backend.servicios.controladores import requiere_nivel
from collections import defaultdict

inscripciones_bp = Blueprint('inscripciones', __name__)

# Formulario de inscripción (GET)
@inscripciones_bp.route('/inscripciones', methods=['GET'])
def formulario_inscripciones():
    # Paises y provincias
    paises_raw = obtener_paises()
    paises = ordenar_paises(paises_raw)
    provincias = obtener_provincias()

    conn = get_connection()
    cursos = []
    cursos_por_nik = defaultdict(list)

    if conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT c.id_curso, c.nombre, c.nikname, c.modalidad, c.dias,
                       c.hora_inicio, c.hora_fin,
                       c.cupo_maximo, c.cupo_espera,
                       (SELECT COUNT(*) FROM inscripciones i 
                        WHERE i.curso_id = c.id_curso AND i.estado='confirmada') AS inscriptos,
                       (SELECT COUNT(*) FROM inscripciones i 
                        WHERE i.curso_id = c.id_curso AND i.estado='espera') AS en_espera
                FROM cursos c
            """)
            cursos = cursor.fetchall()

        conn.close()

    # Armar cursos_por_nik con horarios y modalidad
    for curso in cursos:
        hora_inicio = formatear_hora(curso['hora_inicio'])
        hora_fin = formatear_hora(curso['hora_fin'])
        cursos_por_nik[curso['nikname']].append({
            'id_curso': curso['id_curso'],
            'horario': f"{hora_inicio} a {hora_fin} hs",
            'modalidad': curso['modalidad'],
            'dias': curso['dias']
        })

    return render_template(
        'inscripciones.html',
        paises=paises,
        provincias=provincias,
        cursos=cursos,
        cursos_por_nik=cursos_por_nik
    )



# Guardar inscripción (POST)
@inscripciones_bp.route('/inscribirse', methods=['POST'])
def inscribirse():
    # Convertir el valor de cud a 0/1
    cud_valor = 1 if request.form.get('cud') == 'Si' else 0
    
    curso_id = request.form.get('curso_id')  # Recibimos el curso_id desde el formulario   

    print(">>> curso_id recibido en el POST:", curso_id)

    # 🔎 Validación inicial: que venga un curso_id
    if not curso_id:
        flash("❌ No se seleccionó ningún curso")
        return redirect(url_for('inscripciones.formulario_inscripciones'))

    datos = {
        'apellido': request.form.get('apellido'),
        'nombre': request.form.get('nombre'),
        'dni': request.form.get('dni'),
        'cuil': request.form.get('cuil'),
        'fecha_nacimiento': request.form.get('fecha_nacimiento'),
        'sexo': request.form.get('sexo'),
        'pais_nac': request.form.get('pais_nac'),
        'nacionalidad': request.form.get('nacionalidad'),
        'provincia_nac': request.form.get('provincia_nac'),
        'localidad_nac': request.form.get('localidad_nac'),
        'direccion': request.form.get('direccion'),
        'barrio': request.form.get('barrio'),
        'telefono': request.form.get('telefono'),
        'email': request.form.get('email'),
        'estudios': request.form.get('estudios'),
        'estado_laboral': request.form.get('estado_laboral'),
        'cud': cud_valor,
        'telefono_emergencia': request.form.get('telefono_emergencia'),
    }

    conn = get_connection()
    if conn:
        with conn.cursor() as cursor:

            # 1️⃣ Verificar si el alumno ya existe por DNI o CUIL
            cursor.execute("SELECT id_alumno FROM alumnos WHERE dni = %s OR cuil = %s",
                           (datos['dni'], datos['cuil']))
            alumno = cursor.fetchone()

            if alumno:
                alumno_id = alumno['id_alumno']
            else:
                # 2️⃣ Insertar nuevo alumno
                cursor.execute("""
                    INSERT INTO alumnos (apellido, nombre, dni, cuil, fecha_nacimiento, sexo,
                                        pais_nac, nacionalidad, provincia_nac, localidad_nac, direccion, barrio,
                                        telefono, email, estudios, estado_laboral, cud,
                                        telefono_emergencia, activo)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 1)
                """, (
                    datos['apellido'], datos['nombre'], datos['dni'], datos['cuil'],
                    datos['fecha_nacimiento'], datos['sexo'], datos['pais_nac'], datos['nacionalidad'],
                    datos['provincia_nac'], datos['localidad_nac'], datos['direccion'],
                    datos['barrio'], datos['telefono'], datos['email'], datos['estudios'],
                    datos['estado_laboral'], datos['cud'], datos['telefono_emergencia']
                ))
                alumno_id = cursor.lastrowid

            # 3️⃣ Control de cupos
            cursor.execute("SELECT cupo_maximo, cupo_espera FROM cursos WHERE id_curso = %s", (curso_id,))
            curso = cursor.fetchone()

            # 🔎 Validación: que exista el curso
            if not curso:
                flash("❌ Curso no encontrado en la base de datos")
                return redirect(url_for('inscripciones.formulario_inscripciones'))

            cursor.execute("SELECT COUNT(*) AS total FROM inscripciones WHERE curso_id = %s AND estado='confirmada'", (curso_id,))
            total_confirmados = cursor.fetchone()['total']

            cursor.execute("SELECT COUNT(*) AS total FROM inscripciones WHERE curso_id = %s AND estado='espera'", (curso_id,))
            total_espera = cursor.fetchone()['total']

            if total_confirmados < curso['cupo_maximo']:
                estado = 'confirmada'
                flash("✅ Inscripción confirmada")
            elif total_espera < curso['cupo_espera']:
                estado = 'espera'
                flash("⚠️ El curso está completo, quedaste en lista de espera")
            else:
                flash("❌ No hay más cupo ni lista de espera disponible para este curso")
                return redirect(url_for('inscripciones.formulario_inscripciones'))
            
            # 4️⃣ Registrar inscripción
            cursor.execute("""
                INSERT INTO inscripciones (alumno_id, curso_id, estado)
                VALUES (%s, %s, %s)
            """, (alumno_id, curso_id, estado))

        conn.commit()
        conn.close()
        flash("✅ Inscripción guardada correctamente")
    else:
        flash("❌ Error al conectar con la base de datos")

    return redirect(url_for('inscripciones.formulario_inscripciones'))



@inscripciones_bp.route('/configurar_inscripciones', methods=['GET', 'POST'])
@requiere_nivel('Super', 'Admin')
def configurar_inscripciones():
    estado_actual = 'no'

    conn = get_connection()
    if conn:
        with conn.cursor() as cursor:
            if request.method == 'POST':
                estado = 'si' if 'habilitar' in request.form else 'no'
                cursor.execute(
                    "UPDATE configuracion SET valor = %s WHERE clave = 'inscripciones_habilitadas'",
                    (estado,)
                )
                conn.commit()
                flash('Configuración actualizada')

            cursor.execute(
                "SELECT valor FROM configuracion WHERE clave = 'inscripciones_habilitadas'"
            )
            resultado = cursor.fetchone()
            estado_actual = resultado['valor'] if resultado else 'no'
        conn.close()
    else:
        flash('Error al conectar con la base de datos')

    return render_template('configurar_inscripciones.html', inscripciones_habilitadas=estado_actual)
