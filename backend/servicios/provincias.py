# servicios/provincias.py

from .db import get_connection

def obtener_provincias():
    conn = get_connection()
    if conn is None:
        print("❌ No se pudo conectar a la base de datos")
        return []

    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM provincias ORDER BY nombre ASC")
    provincias = cursor.fetchall()
    conn.close()

    # Convertir a dicts
    provincias = [{'id': p['id'], 'nombre': p['nombre']} for p in provincias]

    return provincias


