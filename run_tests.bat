# Script de ejecución rápida para Windows
# Ejecuta todas las pruebas de login

@echo off
echo ========================================
echo   Ejecutando Pruebas de Login
echo ========================================
echo.

REM Activar entorno virtual si existe
if exist venv\Scripts\activate.bat (
    echo Activando entorno virtual...
    call venv\Scripts\activate.bat
)

echo Ejecutando pruebas...
echo.

python -m pytest tests/test_login.py -v

echo.
echo ========================================
echo   Pruebas Finalizadas
echo ========================================
pause
