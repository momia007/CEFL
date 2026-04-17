# servicios/cursos.py

from .db import get_connection

def insertar_curso(nombre, nikname, descripcion, cuatrimestre, anio, modalidad, activo, hora_inicio, hora_fin, dias):
    conn = get_connection()
    if conn is None:
        print("❌ Error de conexión con la base de datos")
        return

    cursor = conn.cursor()
    sql = """
        INSERT INTO cursos (nombre, nikname, descripcion, cuatrimestre, anio, modalidad, activo, hora_inicio, hora_fin, dias)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (nombre, nikname, descripcion, cuatrimestre, anio, modalidad, activo, hora_inicio, hora_fin, dias))
    conn.commit()
    conn.close()
    return True  # si querés confirmar que se insertó correctamente


def obtener_cursos():
    conn = get_connection()
    cursos = []
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT c.id_curso, c.nombre, c.nikname, c.hora_inicio, c.hora_fin, c.modalidad, c.dias,
                       c.cupo_maximo, c.cupo_espera,
                       (SELECT COUNT(*) FROM inscripciones i WHERE i.curso_id = c.id_curso AND i.estado='Confirmado') AS inscriptos,
                       (SELECT COUNT(*) FROM inscripciones i WHERE i.curso_id = c.id_curso AND i.estado='En espera') AS en_espera
                FROM cursos c
            """)
            cursos = cursor.fetchall()
        conn.close()
    return cursos




