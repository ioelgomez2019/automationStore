@echo off
REM Test E2E - Login
REM Ejecuta los escenarios de autenticación de usuario

echo.
echo ========================================
echo   E2E TEST: LOGIN
echo ========================================
echo.

cd /d "%~dp0"

REM Activar virtualenv si existe
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

REM Ejecutar tests de login con reporte HTML
behave Scenarios/login/login.feature -f behave_html_formatter:HTMLFormatter -o reports/test_e2e_login.html

REM Guardar código de salida
set EXIT_CODE=%ERRORLEVEL%

REM Mostrar resultado
echo.
if %EXIT_CODE% equ 0 (
    echo [SUCCESS] Tests de login completados exitosamente
    echo Reporte disponible en: reports/test_e2e_login.html
) else (
    echo [FAILED] Tests de login fallaron
    echo Reporte disponible en: reports/test_e2e_login.html
)
echo.

exit /b %EXIT_CODE%
