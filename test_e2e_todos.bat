@echo off
REM Test E2E - Suite Completa
REM Ejecuta todos los tests (login + checkout)

echo.
echo ========================================
echo   E2E TEST: SUITE COMPLETA
echo ========================================
echo.

cd /d "%~dp0"

REM Activar virtualenv si existe
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

REM Ejecutar todos los tests con reporte HTML
behave -f behave_html_formatter:HTMLFormatter -o reports/behave_report.html

REM Guardar código de salida
set EXIT_CODE=%ERRORLEVEL%

REM Mostrar resultado
echo.
if %EXIT_CODE% equ 0 (
    echo [SUCCESS] Todos los tests completados exitosamente
) else (
    echo [FAILED] Algunos tests fallaron
)
echo.
echo Reporte disponible en: reports/behave_report.html
echo.

exit /b %EXIT_CODE%
