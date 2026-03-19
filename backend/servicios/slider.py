# cefl\backend\servicios\slider.py

import os

# Carpeta base del proyecto (dos niveles arriba de este archivo)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def obtener_slider(carpeta):
    # Ruta absoluta hacia frontend/static/img/<carpeta>
    ruta = os.path.join(BASE_DIR, 'frontend', 'static', 'img', carpeta)

    if not os.path.exists(ruta):
        return []  # Evita error si la carpeta no existe

    archivos = sorted(os.listdir(ruta))  # orden alfabético

    slider = []
    for archivo in archivos:
        if archivo.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            nombre = os.path.splitext(archivo)[0].replace('_', ' ').capitalize()
            slider.append({
                'img': f'img/{carpeta}/{archivo}',  # importante: ruta relativa para url_for
                'texto': nombre
            })
    return slider
