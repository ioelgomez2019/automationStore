# Script para ejecutar pruebas BDD con Behave en Windows
# Ejecuta todas las pruebas de login usando Behave

@echo off
echo ========================================
echo   Ejecutando Pruebas BDD con Behave
echo ========================================
echo.

REM Activar entorno virtual si existe
if exist venv\Scripts\activate.bat (
    echo Activando entorno virtual...
    call venv\Scripts\activate.bat
)

echo Ejecutando pruebas BDD...
echo.

REM Ejecutar todas las features
behave features/ --format pretty --no-capture

echo.
echo ========================================
echo   Pruebas BDD Finalizadas
echo ========================================
pause
