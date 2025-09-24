import os

def obtener_slider(carpeta):
    print (carpeta);
    ruta = os.path.join('static', 'img', carpeta)
    archivos = sorted(os.listdir(ruta))  # orden alfabético

    slider = []
    for archivo in archivos:
        if archivo.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            nombre = os.path.splitext(archivo)[0].replace('_', ' ').capitalize()
            slider.append({
                'img': f'{carpeta}/{archivo}',
                'texto': nombre  # leyenda automática, podés reemplazarla luego
            })
    return slider
