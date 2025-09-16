#!/bin/bash
# archivo: subir_a_git.sh
version_file="static/version.txt"

# Mostrar estado actual
echo "Estado actual del repositorio:"
git status

# Confirmar acción
read -p "¿Deseás subir los cambios? (S/N): " confirmacion

if [[ "$confirmacion" != "S" && "$confirmacion" != "s" ]]; then
    echo "Abortado por el usuario."
    exit 0
fi

# Obtener fecha actual
fecha=$(date +%d%m%Y)

# Buscar commits previos del día
contador=$(git log --since="midnight" --pretty=oneline | wc -l)

# Generar versión
version="V-${fecha}.${contador}"

# Actualizar version.txt
echo "$version" > "$version_file"
echo "Versión actualizada: $version"

# Subir cambios
git add .
git commit -m "Versión $version"
git push

echo "Cambios subidos correctamente con versión $version."
