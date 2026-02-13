# Automatizacion Login SauceDemo - BDD

Proyecto de automatizacion de pruebas E2E de login en [SauceDemo](https://www.saucedemo.com/) con **Selenium**, **Python** y **arquitectura POM**.

## Contenido

- [Instalacion](#instalacion)
- [Estructura](#estructura)
- [Ejecucion E2E](#ejecucion-e2e)
- [Flujo de capas](#flujo-de-capas)

## Instalacion

### Requisitos
- Python 3.8+
- Google Chrome

### Pasos
```bash
cd j:\Workspace\BANCOPICHINCHA\AutoTestStore
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Estructura

```
AutoTestStore/
├── Scenarios/
│   ├── environment.py
│   ├── steps/
│   │   └── login_steps.py
│   └── login/
│       └── login.feature
├── Script/
│   └── modules/
│       ├── constants/
│       │   └── loginConstants.py
│       ├── data/
│       │   └── loginData.py
│       ├── utils/
│       │   └── loginUtils.py
│       ├── config/
│       │   └── environment.py
│       └── features/
│           └── login/
│               ├── loginPage.py
│               ├── login.py
│               └── loginStep.py
├── behave.ini
└── requirements.txt
```

## Ejecucion E2E

Ejecutar el escenario de login:
```bash
behave Scenarios/login/login.feature
```

Ejecutar por tag:
```bash
behave -t @login
behave -t @smoke
```

### Reporte HTML (opcional)
```bash
pip install behave-html-formatter
behave -f behave_html_formatter:HTMLFormatter -o reports/behave_report.html
```

## Flujo de capas

```
login.feature
  -> loginStep.py
      -> login.py
          -> loginPage.py
              -> mapeos de elementos
```

### Error: "chromedriver no encontrado"
- **Solución**: WebDriver Manager lo descarga automáticamente. Verifica tu conexión a internet.

### Error: "No module named 'selenium'"
- **Solución**: Instala las dependencias: `pip install -r requirements.txt`

### El navegador se cierra demasiado rápido
- **Solución**: Aumenta el `time.sleep()` en el método `tearDown()` o `after_scenario()`

### Error: "element not found"
- **Solución**: Verifica que la página cargó correctamente. Aumenta los timeouts.

### Error: "No steps matched" (Behave)
- **Solución**: Verifica que el texto en el .feature coincida exactamente con los @given/@when/@then

## 🆚 BDD vs Unittest

EstEstructura del Proyecto

```
AutoTestStore/
├── pages/
│   ├── base_page.py           # Clase base
│   └── login_page.py          # Page Object login
├── reports/                    # Reportes HTML
├── test_e2e_visible.py        # Tests con navegador visible
├── test_e2e_headless.py       # Tests en segundo plano
├── run_tests_e2e.bat          # Menu interactivo
├── run_tests_visible.bat      # Ejecutar visible
├── run_tests_headless.bat     # Ejecutar headless
└── requirements.txt           # Dependencias
```

## Documentacion Adicional

- [ARQUITECTURA_POM.md](ARQUITECTURA_POM.md) - Explicacion completa del patron POM
- [GUIA_MAPEO_ELEMENTOS.md](GUIA_MAPEO_ELEMENTOS.md) - Como mapear elementos con DevTools

---

Listo para automatizar!