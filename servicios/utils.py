def formatear_hora(hora_raw):
    try:
        # Si es timedelta
        segundos = hora_raw.seconds
        return f"{segundos // 3600:02}:{(segundos // 60) % 60:02}"
    except AttributeError:
        # Si es datetime.time u otro formato
        return hora_raw.strftime("%H:%M") if hasattr(hora_raw, "strftime") else str(hora_raw)

# Para actualizar leyenda de la version actual
def obtener_version():
    try:
        with open("static/version.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "desconocida"