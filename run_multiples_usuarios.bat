@echo off
echo ========================================
echo   TEST CON MULTIPLES USUARIOS
echo ========================================
echo.

REM Activar entorno virtual si existe
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

echo Probara login con 4 usuarios diferentes:
echo   1. standard_user (exitoso)
echo   2. locked_out_user (bloqueado)
echo   3. usuario_invalido (error)
echo   4. problem_user (exitoso)
echo.
pause

python test_multiples_usuarios.py

pause
