# cefl\backend\servicios\utils.py
import os

def formatear_hora(hora_raw):
    try:
        # Si es timedelta
        segundos = hora_raw.seconds
        return f"{segundos // 3600:02}:{(segundos // 60) % 60:02}"
    except AttributeError:
        # Si es datetime.time u otro formato
        return hora_raw.strftime("%H:%M") if hasattr(hora_raw, "strftime") else str(hora_raw)

# Para actualizar leyenda de la version actual
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def obtener_version():
    ruta = os.path.join(BASE_DIR, 'frontend', 'static', 'version.txt')
    print("Ruta buscada:", ruta)  # 🧪 Depuración
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        return "versión desconocida"

    
def ordenar_paises(paises):
    if not paises:
        return []

    paises_dict = [{'id': p['id'], 'nombre': p['nombre']} for p in paises if 'id' in p and 'nombre' in p]

    return sorted(
        paises_dict,
        key=lambda p: (p['nombre'].strip().lower() == 'otro', p['nombre'].lower())
    )
