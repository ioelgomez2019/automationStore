AUTOTESTSTORE - EJECUCION PASO A PASO
=====================================

Objetivo
--------
Ejecutar los escenarios E2E (login y checkout) con Behave + Selenium en un entorno controlado.

Versiones de tecnologias
------------------------
- Python: 3.10 o superior
- Selenium: 4.15.0
- Behave: 1.2.6+
- webdriver-manager: 4.0.1
- behave-html-formatter: 0.9.10
- Google Chrome: version estable mas reciente
- Git: version estable mas reciente

Requisitos previos
------------------
- Windows, macOS o Linux
- Git instalado y en PATH
- Python 3.10+ instalado y en PATH
- Chrome instalado

Opcion A (primera vez, setup automatico)
----------------------------------------
Windows:
1) Descargar setup_windows.bat
2) Doble click en setup_windows.bat
3) Esperar 3-5 minutos
4) Abrir reporte: AutoTestStore\reports\behave_report.html

macOS / Linux:
1) Descargar setup_macos_linux.sh
2) Abrir terminal en la carpeta destino
3) Ejecutar:
   chmod +x setup_macos_linux.sh
   ./setup_macos_linux.sh
4) Abrir reporte: AutoTestStore/reports/behave_report.html

Opcion B (manual, paso a paso)
------------------------------
1) Clonar repositorio:
   git clone https://github.com/ioelgomez2019/automationStore.git

2) Entrar al proyecto:
   cd AutoTestStore

3) Crear entorno virtual:
   python -m venv venv

4) Activar entorno virtual:
   Windows: venv\Scripts\activate
   macOS/Linux: source venv/bin/activate

5) Instalar dependencias:
   pip install -r requirements.txt

6) Ejecutar tests:
   - Todos:
     behave -f behave_html_formatter:HTMLFormatter -o reports/behave_report.html
   - Login:
     behave Scenarios/login/login.feature -f behave_html_formatter:HTMLFormatter -o reports/test_e2e_login.html
   - Checkout:
     behave Scenarios/checkout/checkout.feature -f behave_html_formatter:HTMLFormatter -o reports/test_e2e_compra.html

7) Ver reportes HTML:
   - reports/behave_report.html
   - reports/test_e2e_login.html
   - reports/test_e2e_compra.html

Ejecucion rapida con scripts (post-setup)
-----------------------------------------
Windows:
- test_e2e_login.bat
- test_e2e_comprar_producto.bat
- test_e2e_todos.bat
- test_e2e_smoke.bat

PowerShell:
- .\test_e2e_login.ps1
- .\test_e2e_comprar_producto.ps1
- .\test_e2e_todos.ps1
- .\test_e2e_smoke.ps1

Notas
-----
- Si falla la ejecucion, revisar reports/behave_report.html
- Si no reconoce comandos, reactivar el virtualenv
- Para mas detalle, ver DOCUMENTACION_PROYECTO.md
