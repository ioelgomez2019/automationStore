# Script para ejecutar pruebas BDD con tags específicos

@echo off
echo ========================================
echo   Ejecutar Pruebas BDD por Tags
echo ========================================
echo.

REM Activar entorno virtual si existe
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

:MENU
echo.
echo Selecciona el tipo de prueba a ejecutar:
echo.
echo 1. Todas las pruebas
echo 2. Solo pruebas de Smoke (@smoke)
echo 3. Solo pruebas exitosas (@exitoso)
echo 4. Solo pruebas de error (@error)
echo 5. Solo pruebas críticas (@critical)
echo 6. Generar reporte HTML
echo 7. Salir
echo.
set /p choice="Ingresa tu opcion (1-7): "

if "%choice%"=="1" goto ALL
if "%choice%"=="2" goto SMOKE
if "%choice%"=="3" goto SUCCESS
if "%choice%"=="4" goto ERROR
if "%choice%"=="5" goto CRITICAL
if "%choice%"=="6" goto REPORT
if "%choice%"=="7" goto END

echo Opcion invalida. Intenta de nuevo.
goto MENU

:ALL
echo.
echo Ejecutando TODAS las pruebas...
behave features/ --format pretty --no-capture
goto END_TESTS

:SMOKE
echo.
echo Ejecutando pruebas de SMOKE...
behave features/ --tags=@smoke --format pretty --no-capture
goto END_TESTS

:SUCCESS
echo.
echo Ejecutando pruebas EXITOSAS...
behave features/ --tags=@exitoso --format pretty --no-capture
goto END_TESTS

:ERROR
echo.
echo Ejecutando pruebas de ERROR...
behave features/ --tags=@error --format pretty --no-capture
goto END_TESTS

:CRITICAL
echo.
echo Ejecutando pruebas CRITICAS...
behave features/ --tags=@critical --format pretty --no-capture
goto END_TESTS

:REPORT
echo.
echo Generando reporte HTML...
behave features/ --format html --outfile reports/behave_report.html --format pretty
echo.
echo Reporte generado en: reports/behave_report.html
goto END_TESTS

:END_TESTS
echo.
echo ========================================
echo   Pruebas Finalizadas
echo ========================================
pause
goto MENU

:END
echo.
echo Saliendo...
