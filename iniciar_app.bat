@echo off
echo Activando entorno virtual...
call venv\Scripts\activate

echo Iniciando la aplicación Flask...
start "" http://127.0.0.1:5000
start /B python app.py
pause