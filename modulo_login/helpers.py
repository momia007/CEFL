# validaciones, carga de variables

def cargar_contexto_usuario(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    contexto = {
        'nombre': usuario.nombre,
        'rol': usuario.rol,
        'empresa_id': usuario.empresa_id,
        # más variables según el proyecto
    }
    return contexto
