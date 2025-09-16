from .db import get_connection

def obtener_paises():
    conn = get_connection()
    if conn is None:
        print("❌ No se pudo conectar a la base de datos")
        return []

    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM paises ORDER BY nombre ASC")
    paises = cursor.fetchall()
    conn.close()
    return paises

from .db import get_connection

