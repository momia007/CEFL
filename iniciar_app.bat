@echo off
echo Cerrando procesos Python previos...
taskkill /F /IM python.exe >nul 2>&1

echo Activando entorno virtual...
call venv\Scripts\activate

echo Iniciando la aplicacion Flask...
start "" http://127.0.0.1:5000
start /B python app.py
pause