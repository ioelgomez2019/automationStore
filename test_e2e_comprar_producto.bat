@echo off
REM Test E2E - Compra de Producto
REM Ejecuta el flujo completo: login -> seleccionar producto -> carrito -> checkout -> confirmación

echo.
echo ========================================
echo   E2E TEST: COMPRA DE PRODUCTO
echo ========================================
echo.

cd /d "%~dp0"

REM Activar virtualenv si existe
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

REM Ejecutar tests de checkout con reporte HTML
behave Scenarios/checkout/checkout.feature -f behave_html_formatter:HTMLFormatter -o reports/test_e2e_compra.html

REM Guardar código de salida
set EXIT_CODE=%ERRORLEVEL%

REM Mostrar resultado
echo.
if %EXIT_CODE% equ 0 (
    echo [SUCCESS] Test de compra completado exitosamente
    echo Reporte disponible en: reports/test_e2e_compra.html
) else (
    echo [FAILED] Test de compra fallido
    echo Reporte disponible en: reports/test_e2e_compra.html
)
echo.

exit /b %EXIT_CODE%
