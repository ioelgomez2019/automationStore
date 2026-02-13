VERSION=0.1.0-beta
RELEASE_DATE=2026-02-13
STATUS=Beta

CHANGELOG:
==========

v0.1.0-beta (2026-02-13)
------------------------
✅ FEATURES
- Login automatizado con credenciales paramétricos
- Flujo completo de compra (inventario → carrito → checkout → confirmación)
- 2 escenarios principales (login + compra) con ejemplos paramétricos
- Reportes HTML automáticos

✅ ARQUITECTURA
- BDD con Behave y Gherkin en español
- Page Object Model (POM) - 6 capas
- Separación completa: Features → Steps → Logic → Pages → Utilities
- BasePage con helpers comunes para Selenium
- Wait strategies optimizadas

✅ OPTIMIZACIONES
- Velocidad: ~9 segundos por escenario
- Búsquedas inteligentes (sin wait innecesarios)
- Chrome options optimizadas (sin popups)
- Manejo de timeouts eficiente

✅ DOCUMENTACIÓN
- DOCUMENTACION_PROYECTO.md (guía completa)
- QUICK_START.txt (inicio rápido)
- Scripts ejecutables (.bat y .ps1)
- Código bien comentado

✅ SCRIPTS DE EJECUCIÓN
- test_e2e_login.bat/ps1
- test_e2e_comprar_producto.bat/ps1
- test_e2e_todos.bat/ps1
- test_e2e_smoke.bat/ps1

PRÓXIMA VERSIÓN (v0.2.0):
=========================
- Filter/búsqueda de productos
- Sorting por precio/nombre
- Carrito con cantidad variable
- Validación de descuentos
- Tests paralelos

LIMITACIONES CONOCIDAS:
=======================
- Solo Chrome (no soporta Firefox/Edge aún)
- Solo aplicación SauceDemo (no parametrizable)
- No incluye tests de performance
- No incluye visual regression testing

REQUISITOS:
===========
- Python 3.10+
- Chrome instalado
- 500MB espacio libre
- Internet para descargar drivers

INSTALACIÓN:
============
pip install -r requirements.txt

EJECUCIÓN:
==========
test_e2e_comprar_producto.bat

SOPORTE:
========
Para issues/consultas, revisar:
1. QUICK_START.txt
2. DOCUMENTACION_PROYECTO.md (sección 9 - Troubleshooting)
3. Reportes HTML en reports/
