@echo off
REM Test E2E - Smoke Tests (Críticos)
REM Ejecuta solo los tests marcados como @smoke

echo.
echo ========================================
echo   E2E TEST: SMOKE (CRITICOS)
echo ========================================
echo.

cd /d "%~dp0"

REM Activar virtualenv si existe
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

REM Ejecutar solo tests críticos con reporte HTML
behave --tags=@smoke -f behave_html_formatter:HTMLFormatter -o reports/test_e2e_smoke.html

REM Guardar código de salida
set EXIT_CODE=%ERRORLEVEL%

REM Mostrar resultado
echo.
if %EXIT_CODE% equ 0 (
    echo [SUCCESS] Smoke tests completados exitosamente
) else (
    echo [FAILED] Smoke tests fallaron
)
echo.
echo Reporte disponible en: reports/test_e2e_smoke.html
echo.

exit /b %EXIT_CODE%
