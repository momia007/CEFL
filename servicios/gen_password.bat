@echo off
setlocal enabledelayedexpansion

:: Pedir contraseña oculta usando PowerShell
for /f "delims=" %%P in ('powershell -Command "$p = Read-Host -AsSecureString 'Ingresá la contraseña'; [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($p))"') do set "password=%%P"

for /f "delims=" %%C in ('powershell -Command "$p = Read-Host -AsSecureString 'Confirmá la contraseña'; [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($p))"') do set "confirm=%%C"

:: Comparar contraseñas
if not "!password!"=="!confirm!" (
    echo ❌ Las contraseñas no coinciden. Abortando.
    pause
    exit /b
)

:: Generar hash SHA-256 correctamente
for /f "delims=" %%H in ('powershell -Command "[System.BitConverter]::ToString([System.Security.Cryptography.SHA256]::Create().ComputeHash([System.Text.Encoding]::UTF8.GetBytes('%password%'))).Replace('-','')"') do set "hash=%%H"

:: Mostrar y copiar
echo ✅ Hash generado: !hash!
echo !hash! | clip
echo 📋 Hash copiado al portapapeles

pause

