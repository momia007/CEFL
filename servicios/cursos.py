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
    if conn is None:
        print("❌ No se pudo conectar a la base de datos")
        return []

    cursor = conn.cursor()
    # ⚠️ Corrección: FROM cursos, no paises. WHERE va antes de ORDER BY
    cursor.execute("""
        SELECT 
            id_curso,
            nombre,
            nikname,
            descripcion,
            cuatrimestre,
            anio,
            modalidad,
            hora_inicio,
            hora_fin,
            dias,
            activo
        FROM cursos
        ORDER BY hora_inicio ASC
    """)
    cursos = cursor.fetchall()
    conn.close()
    return cursos

