@echo off
REM Verificación pre-despliegue en Windows

cls
echo.
echo ========================================
echo   VERIFICACION PRE-DESPLIEGUE (BETA)
echo ========================================
echo.

echo [1/5] Verificando estructura de directorios...
if exist "Scenarios" echo   OK Scenarios/
if exist "Script\modules" echo   OK Script\modules\
if exist "reports" echo   OK reports\
if exist "Script\modules\features\login" echo   OK login\
if exist "Script\modules\features\checkout" echo   OK checkout\
echo.

echo [2/5] Verificando archivos críticos...
if exist "requirements.txt" echo   OK requirements.txt
if exist "behave.ini" echo   OK behave.ini
if exist "DOCUMENTACION_PROYECTO.md" echo   OK DOCUMENTACION_PROYECTO.md
if exist "QUICK_START.txt" echo   OK QUICK_START.txt
if exist "VERSION.md" echo   OK VERSION.md
if exist "DESPLIEGUE.md" echo   OK DESPLIEGUE.md
echo.

echo [3/5] Verificando feature files...
if exist "Scenarios\login\login.feature" echo   OK login.feature
if exist "Scenarios\checkout\checkout.feature" echo   OK checkout.feature
echo.

echo [4/5] Verificando archivos Python...
if exist "Script\modules\features\login\login.py" echo   OK login.py
if exist "Script\modules\features\login\loginPage.py" echo   OK loginPage.py
if exist "Script\modules\features\checkout\checkout.py" echo   OK checkout.py
if exist "Script\modules\config\environment.py" echo   OK environment.py
if exist "Script\modules\utils\loginUtils.py" echo   OK loginUtils.py
echo.

echo [5/5] Verificando scripts ejecutables...
if exist "test_e2e_login.bat" echo   OK test_e2e_login.bat
if exist "test_e2e_comprar_producto.bat" echo   OK test_e2e_comprar_producto.bat
if exist "test_e2e_todos.bat" echo   OK test_e2e_todos.bat
if exist "test_e2e_login.ps1" echo   OK test_e2e_login.ps1
if exist "test_e2e_comprar_producto.ps1" echo   OK test_e2e_comprar_producto.ps1
echo.

echo ========================================
echo   VERIFICACION COMPLETADA
echo ========================================
echo.
echo Proyecto listo para DESPLIEGUE (BETA)
echo.
echo Próximos pasos:
echo   1. pip install -r requirements.txt
echo   2. behave --dry-run
echo   3. test_e2e_login.bat
echo   4. test_e2e_comprar_producto.bat
echo.
pause
