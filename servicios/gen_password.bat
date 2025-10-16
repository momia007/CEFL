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

:: Generar hash SHA-256
echo !password! | powershell -Command "[Text.Encoding]::UTF8.GetBytes((Get-Content -Raw -)) | % { $_ } | ConvertTo-SecureString -AsPlainText -Force | ConvertFrom-SecureString | Out-String" > nul
for /f %%H in ('echo !password! ^| powershell -Command "Get-FileHash -Algorithm SHA256 -InputStream ([System.IO.MemoryStream]::new([System.Text.Encoding]::UTF8.GetBytes((Get-Content -Raw -)))) | Select-Object -ExpandProperty Hash"') do set "hash=%%H"

echo ✅ Hash generado: !hash!

:: Copiar al portapapeles
echo !hash! | clip
echo 📋 Hash copiado al portapapeles

pause
