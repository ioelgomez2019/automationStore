@echo off
echo ========================================
echo   TEST DE LOGIN COMPLETO (POM)
echo ========================================
echo.

REM Activar entorno virtual si existe
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

echo Este test hara login real en SauceDemo
echo usando la arquitectura Page Object Model
echo.
pause

python test_login_completo.py

pause
